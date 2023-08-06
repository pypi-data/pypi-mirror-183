from __future__ import annotations
from functools import lru_cache
from typing import Dict, List, Optional

from .member import Member
from .client import client
from .message import Message
from .util import Waiter, fetch_cursored


class Channel:
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        creator: Member,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.creator = creator

    @property
    def mention(self) -> str:
        return f"<#{self.id}>"

    def invite(self, members: List[Member]):
        Waiter(tire=3)
        client().conversations_invite(
            channel=self.id, users=[member.id for member in members]
        )

        Message.post(
            self,
            f"""{len(members)}人を{self.name}に招待しました
招待者リスト: {", ".join([member.name for member in members])}
""",
        )

    @property
    def members(self) -> List[Member]:
        response = fetch_cursored(
            lambda cursor: client().conversations_members(
                cursor=cursor, channel=self.id
            ),
            "members",
            tire=4,
        )
        return [Member.fetch(member_id) for member_id in response]

    @staticmethod
    @lru_cache()
    def fetch_all() -> Dict[str, Channel]:
        response = fetch_cursored(
            lambda cursor: client().conversations_list(
                cursor=cursor,
                exclude_archived=True,
                types="public_channel,private_channel,mpim,im",
            ),
            "channels",
            tire=2,
        )

        channels = [
            Channel(
                channel["id"],
                channel["name"],
                channel["purpose"]["value"],
                Member.fetch(channel["creator"]),
            )
            for channel in response
        ]
        id_list = [channel.id for channel in channels]

        return dict(zip(id_list, channels))

    @classmethod
    def fetch(
        cls, *, channel_id: Optional[str] = None, channel_name: Optional[str] = None
    ):
        """channel_id もしくは channel_name でチャンネルを検索し返す"""
        def query_by_id(channel_id: str):
            return cls.fetch_all().get(channel_id, None)

        def query_by_name(channel_name: str):
            channels: List[Channel] = list(cls.fetch_all().values())
            channel_names: List[str] = [channel.name for channel in cls.fetch_all().values()]

            try:
                return channels[channel_names.index(channel_name)]
            except ValueError:
                return None

        assert (channel_id is None or channel_name is None) and (
            channel_id is not None and channel_name is not None
        )

        if channel_id is not None:
            channel = query_by_id(channel_id)
            if channel is not None:
                return channel

            # キャッシュを削除する
            cls.fetch_all.cache_clear()

            channel = query_by_id(channel_id)
            if channel is not None:
                return channel

            # それでも見つからない場合
            raise RuntimeError(f"Channel id {channel_id} not found")
        else:
            # channel_name is not None
            channel = query_by_name(channel_name)
            if channel is not None:
                return channel

            # キャッシュを削除する
            cls.fetch_all.cache_clear()

            channel = query_by_name(channel_name)
            if channel is not None:
                return channel

            # それでも見つからない場合
            raise RuntimeError(f"Channel name {channel_name} not found")


    @classmethod
    def fetch_by_response(cls, response: Dict[str, str]) -> Channel:
        if response.get("channel_type", "") == "im":
            # DMの場合
            return cls(
                response["channel"],
                response["user"],
                "",
                Member.fetch(response["user"]),
            )
        else:
            return cls.fetch(channel_id=response.get("channel", ""))

    def post(
        self,
        message: str,
        *,
        image_url: Optional[str] = None,
        reply2: Optional[Message] = None,
        reply2channel: bool = False,
    ):
        def _blocks():
            if image_url is None:
                return None
            else:
                return [
                    {
                        "type": "section",
                        "text": {"type": "plain_text", "text": message},
                    },
                    {
                        "type": "image",
                        "image_url": image_url,
                        "alt_text": "image is not loaded",
                    },
                ]

        if reply2 is None:
            reply2 = Message(self, "", "", "")

        Waiter(tire=3)
        response: Dict = client().chat_postMessage(
            channel=self.id,
            text=message,
            thread_ts=reply2.timestamp,
            reply_broadcast=reply2channel,
            blocks=_blocks(),
        )  # type: ignore

        return Message(self, message, response["ts"], reply2.timestamp)
