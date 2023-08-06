import base64
from datetime import datetime
from uuid import UUID

from dateutil import parser
import pytz
import timeago


def format_time(timestamp: str) -> str:
    dt = parser.isoparse(timestamp)
    return timeago.format(dt, datetime.now(tz=pytz.UTC))


def format_uuid(uuid: str) -> str:
    return base64.urlsafe_b64encode(UUID(uuid).bytes).decode().replace('=', '')


def parse_uuid(uuid: str) -> UUID:
    return UUID(bytes=base64.urlsafe_b64decode(f"{uuid}=="))
