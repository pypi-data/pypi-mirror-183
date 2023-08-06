from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, Optional

from util import Waiter
from client import client

if TYPE_CHECKING:
    from channel import Channel



@dataclass
class Message:
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

    @staticmethod
    def post(
        channel: Channel,
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
            reply2 = Message(channel, "", "", "")

        Waiter(tire=3)
        response: Dict = client().chat_postMessage(
            channel=channel.id,
            text=message,
            thread_ts=reply2.timestamp,
            reply_broadcast=reply2channel,
            blocks=_blocks(),
        )  # type: ignore

        return Message(channel, message, response["ts"], reply2.timestamp)
