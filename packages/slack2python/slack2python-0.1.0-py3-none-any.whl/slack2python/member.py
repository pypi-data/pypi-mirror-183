from __future__ import annotations
from functools import lru_cache
from typing import Dict

from client import client
from util import Waiter, fetch_cursored


class Member:
    """メンバー1人を表現するクラス
    __init__(), fetch()の2つの初期化方法がある
    """

    def __init__(
        self,
        id: str,
        name: str,
    ):
        self.id = id
        self.name = name

    @property
    def mention(self) -> str:
        return f"<@{self.id}>"

    @staticmethod
    @lru_cache()
    def fetch_all() -> Dict[str, Member]:
        """ワークスペースに存在するアカウントをすべて問い合わせる
        botや解約済みアカウントなどは省く
        """

        def _is_valid_member(member: Dict) -> bool:
            """そのmemberがbotなのかユーザーなのか判定する"""

            def _has_prohibited_keys(member: Dict):
                """botや解約済みのプロパティを持っているか判定する"""
                # 以下の属性が1つでもtrueだと省きたい
                prohibited_keys = [
                    "is_bot",
                    "deleted",
                    "is_restricted",
                    "is_ultra_restricted",
                ]
                return sum([member.get(key, 0) for key in prohibited_keys]) != 0

            def _is_slackbot(member: Dict):
                """slackbotかどうか判定する
                slackbotは _has_prohibited_keywards に該当しないため"""

                return member["id"] == "USLACKBOT"

            return not _has_prohibited_keys(member) and not _is_slackbot(member)

        members = fetch_cursored(
            lambda cursor: client().users_list(cursor=cursor, exclude_arrived=True),
            "members",
            2,
        )
        members = [Member(member["id"], member["profile"]["real_name"]) for member in members if _is_valid_member(member)]
        keys = [member.id for member in members]
        return dict(zip(keys, members))

    @classmethod
    @lru_cache
    def fetch(cls, member_id: str) -> Member:
        # return fetch_all()'s member to avoid ask slack server frequently
        if member_id in cls.fetch_all().keys():
            return cls.fetch_all()[member_id]

        # キャッシュを削除して、slack serverに問い合わせる
        cls.fetch_all.cache_clear()
        if member_id in cls.fetch_all().keys():
            return cls.fetch_all()[member_id]

        # それでもない場合、botなどの可能性があるので個別に問い合わせる
        Waiter(tire=4)
        response: Dict = client().users_info(user=member_id)  # type: ignore
        if response["ok"] == False and response["error"] != "user_not_found":
            raise ValueError(f"Invalid member id: {member_id}")
        else:
            return Member(
                response["user"]["id"], response["user"]["profile"]["real_name"]
            )

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
