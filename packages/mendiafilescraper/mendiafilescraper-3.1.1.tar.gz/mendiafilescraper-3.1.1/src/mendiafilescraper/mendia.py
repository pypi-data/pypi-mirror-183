import asyncio
import json
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional

import websockets
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Movie:
    title: str
    year: int
    size: int
    hash: str
    tmdb_id: int
    audio_languages: str
    subtitle_languages: str
    resolution: str
    dynamic_range: str
    bitrate: int
    sent: bool


@dataclass_json
@dataclass
class PushMovies:
    type: str
    username: str
    api_key: str
    movies: List[Movie]


@dataclass_json
@dataclass
class PushMoviesResult:
    success: bool
    reason: str


@dataclass_json
@dataclass
class GetTMDbApiKey:
    type: str
    username: str
    api_key: str


@dataclass_json
@dataclass
class GetTMDbApiKeyResult:
    tmdb_api_key: Optional[str]


@dataclass_json
@dataclass
class LoginCredentials:
    type: str
    username: str
    password: str


@dataclass_json
@dataclass
class LoginFailed:
    type: str
    reason: str


@dataclass_json
@dataclass
class Session:
    type: str
    username: str
    api_key: str


async def get_tmdb_api_key(
    server_address: str, username: str, password: str
) -> Optional[str]:
    try:
        async with websockets.connect(server_address) as websocket:
            await websocket.send(
                LoginCredentials(
                    type="LoginCredentials", username=username, password=password
                ).to_json()
            )
            message = await asyncio.wait_for(websocket.recv(), timeout=10)

            message: Dict = json.loads(message)
            if "type" in message.keys() and message["type"] == "Session":
                session: Session = Session.from_dict(message)
            elif "type" in message.keys() and message["type"] == "LoginFailed":
                failed: LoginFailed = LoginFailed.from_dict(message)
                logging.error("Login failed: %s", failed.reason)
                return None
            else:
                logging.error("Received unexpected message: %s", str(message))
                return None
            cmd = GetTMDbApiKey(
                type="GetTMDbApiKey",
                username=username,
                api_key=session.api_key,
            )

            await websocket.send(cmd.to_json())
            message = await asyncio.wait_for(websocket.recv(), timeout=10)

            message: Dict = json.loads(message)
            if "type" in message.keys() and message["type"] == "GetTMDbApiKeyResult":
                cmd_result: GetTMDbApiKeyResult = GetTMDbApiKeyResult.from_dict(message)
                if not cmd_result.tmdb_api_key:
                    logging.error(
                        "Failed to acquire tmdb api key! Mendia gave the following reason: %s",
                        cmd_result.reason,
                    )
                    return None
                return cmd_result.tmdb_api_key
            logging.error(
                "Failed to acquire tmdb api key! Mendia did not send a GetTMDbApiKeyResult."
            )
            return None
    except Exception:
        logging.exception(
            "The websocket connection to '%s' could not be established or failed.",
            server_address,
        )
        return None


async def publish_movies(
    server_address: str, username: str, password: str, movies: List[Movie]
) -> bool:
    push_msg = PushMovies(
        type="PushMovies", username=username, api_key="", movies=movies
    )
    logging.info("Publishing to %s", server_address)

    try:
        async with websockets.connect(server_address) as websocket:
            await websocket.send(
                LoginCredentials(
                    type="LoginCredentials", username=username, password=password
                ).to_json()
            )
            message = await asyncio.wait_for(websocket.recv(), timeout=10)

            message: Dict = json.loads(message)
            if "type" in message.keys() and message["type"] == "Session":
                session: Session = Session.from_dict(message)
            elif "type" in message.keys() and message["type"] == "LoginFailed":
                failed: LoginFailed = LoginFailed.from_dict(message)
                logging.error("Login failed: %s", failed.reason)
                return False
            else:
                logging.error("Received unexpected message: %s", str(message))
                return False
            push_msg.api_key = session.api_key

            await websocket.send(push_msg.to_json())
            message = await asyncio.wait_for(websocket.recv(), timeout=10)

            message: Dict = json.loads(message)
            if "type" in message.keys() and message["type"] == "PushMoviesResult":
                push_message_result: PushMoviesResult = PushMoviesResult.from_dict(
                    message
                )
                if not push_message_result.success:
                    logging.error(
                        "Failed to push new movies! Mendia gave the following reason: %s",
                        push_message_result.reason,
                    )
                    return False
            else:
                logging.error(
                    "Failed to push new movies! Mendia did not send a PushMovieResult."
                )
                return False
    except Exception:
        logging.exception(
            "The websocket connection to '%s' could not be established or failed.",
            server_address,
        )
        return False
    logging.info("Pushed movies successfully!")
    return True
