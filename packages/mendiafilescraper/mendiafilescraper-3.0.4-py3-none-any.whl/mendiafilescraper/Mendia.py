import asyncio
import json
import logging
from dataclasses import dataclass
from typing import Dict, List

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


async def publish_movies(
    server_address: str, username: str, password: str, movies: List[Movie]
) -> bool:
    push_msg = PushMovies(
        type="PushMovies", username=username, api_key="", movies=movies
    )
    logging.info(f"Publishing to {server_address}")

    try:
        async with websockets.connect(server_address) as websocket:
            await websocket.send(
                LoginCredentials(
                    type="LoginCredentials", username=username, password=password
                ).to_json()
            )
            message = await asyncio.wait_for(websocket.recv(), timeout=10)

            object: Dict = json.loads(message)
            if "type" in object.keys() and object["type"] == "Session":
                session: Session = Session.from_dict(object)
            elif "type" in object.keys() and object["type"] == "LoginFailed":
                failed: LoginFailed = LoginFailed.from_dict(object)
                logging.error("Login failed: %s", failed.reason)
                return False
            else:
                logging.error("Received unexpected message: %s", str(object))
                return False
            push_msg.api_key = session.api_key

            await websocket.send(push_msg.to_json())
            message = await asyncio.wait_for(websocket.recv(), timeout=10)

            object: Dict = json.loads(message)
            if "type" in object.keys() and object["type"] == "PushMoviesResult":
                push_message_result: PushMoviesResult = PushMoviesResult.from_dict(
                    object
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
