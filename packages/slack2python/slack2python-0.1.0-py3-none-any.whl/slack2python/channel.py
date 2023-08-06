from __future__ import annotations
from functools import lru_cache
from typing import Dict, List

from member import Member
from client import client
from message import Message
from util import Waiter, fetch_cursored


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
            tire=4
        )
        return [Member.fetch(member_id) for member_id in response]

    @staticmethod
    @lru_cache()
    def fetch_all():
        response = fetch_cursored(
            lambda cursor: client().conversations_list(
                cursor=cursor, exclude_archived=True
            ),
            "channels",
            tire=2
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
    def fetch_public_channel(cls, channel_id: str):
        channels = cls.fetch_all()
        if channel_id in channels.keys():
            return channels[channel_id]

        # キャッシュを削除する
        cls.fetch_all.cache_clear()
        channels = cls.fetch_all()
        if channel_id in channels.keys():
            return channels[channel_id]

        # それでも見つからない場合
        raise RuntimeError(f"Channel id {channel_id} not found")

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
            return cls.fetch_public_channel(response.get("channel", ""))
