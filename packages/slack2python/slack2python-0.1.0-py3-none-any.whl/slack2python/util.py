from datetime import datetime, timedelta
from time import sleep
from typing import Callable, Dict, List

from slack_sdk.web import SlackResponse


class Waiter:
    """SlackのRateLimitを回避するために一定時間待つクラス"""

    last_executed_time: Dict[int, datetime] = dict(
        [(i, datetime.now()) for i in range(1, 5)]
    )
    time_required: Dict[int, timedelta] = {
        1: timedelta(seconds=60 / 1),
        2: timedelta(seconds=60 / 20),
        3: timedelta(seconds=60 / 50),
        4: timedelta(seconds=60 / 100),
    }

    def __init__(self, *, tire: int):
        """tireごとに必要な時間までsleepする

        Args:
            tire (int): tire. please read https://api.slack.com/docs/rate-limits
        """
        if self.required_seconds(tire=tire) > 0:
            Waiter.last_executed_time[tire] = datetime.now() + timedelta(
                seconds=self.required_seconds(tire=tire)
            )
            sleep(self.required_seconds(tire=tire))
        else:
            Waiter.last_executed_time[tire] = datetime.now()

    @classmethod
    def required_seconds(cls, *, tire: int) -> float:
        elapsed_time = datetime.now() - Waiter.last_executed_time[tire]
        required_time = Waiter.time_required[tire] - elapsed_time

        if required_time.total_seconds() < 0:
            return 0
        else:
            return required_time.total_seconds()


def fetch_cursored(
    fetcher: Callable[[str], SlackResponse], concat_name: str, tire: int
) -> List:
    """next_cursorを使って分割ダウンロードを行う

    Args:
        fetcher (Callable[[str], SlackResponse]): next_cursorを引数として、Slack Web APIから受けとったSlackResponseを返すような関数
        concat_name (str): 分割してダウンロードしたレスポンスを1つにまとめるときのキー
        tire (int): ダウンロードするAPIのTire

    Returns:
        List: ダウンロードした結果を1つにまとめて返す
    """
    result: List = []
    next_cursor = ""
    while True:
        Waiter(tire=tire)

        response: Dict = fetcher(next_cursor)  # type: ignore
        next_cursor = response["response_metadata"]["next_cursor"]
        result.extend(response[concat_name])

        if next_cursor == "":
            break

    return result
