from typing import Optional
from slack_bolt import App
from slack_sdk import WebClient

_app: Optional[App] = None
_client: Optional[WebClient] = None

def raise_uninitialized_error():
    raise RuntimeError("Please use init() to initialize slack2python")

def app() -> App:
    if _app is None:
        raise_uninitialized_error()
    return _app

def client() -> WebClient:
    if _client is None:
        raise_uninitialized_error()
    return _client

def init(bot_user_oauth_token: str, signing_secret: str):
    """initialize slack2python

    To get the arguments of this function, follow the steps.
    1. Go to https://api.slack.com/apps/
    2. Click your app
    3. Copy 'Singing Secret'
    4. Click 'OAuth & Permissions'
    5. Add at least 1 bot token scopes if no scope registered
    6. Copy 'Bot User OAuth Token'

    Args:
        bot_user_oauth_token (str): Bot User OAuth Token
        signing_secret (str): Singing Secret
    """
    global _app, _client

    if _app is not None or _client is not None:
        raise RuntimeError("init() cannot be executed twice or more")

    _app = App(
        token=bot_user_oauth_token,
        signing_secret=signing_secret,
    )
    _client = _app.client

def start(port: int=8000):
    """start a slack bolt session

    Args:
        port (int): port to listen slack events
    """
    app().start(port=port)
