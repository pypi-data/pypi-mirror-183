from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, Optional

from .util import Waiter
from .client import client

if TYPE_CHECKING:
    from .channel import Channel


@dataclass
class Message:
    """メッセージを表現するクラス"""

    channel: Channel
    text: str
    timestamp: str
    root_timestamp: str = ""

    def add_reaction(self, reaction_name: str):
        Waiter(tire=3)
        client().reactions_add(
            channel=self.channel.id, name=reaction_name, timestamp=self.timestamp
        )

    def update(self, new_message: str):
        self.text = new_message
        Waiter(tire=3)
        client.chat_update(channel=self.channel.id, ts=self.timestamp, text=self.text)
