import os
import time
import json
from pathlib import Path
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#from twilio.rest import Client

class ActionSessionStart(Action):
    def name(self) -> str:
        return "action_session_start"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: dict) -> list:
        # Get the call metadata from the tracker
        metadata = tracker.get_slot("session_started_metadata")
        # Set appropriate slots
        if metadata:
            return [
                SlotSet("user_phone", metadata.get("user_phone")),
                SlotSet("bot_phone", metadata.get("bot_phone")),
            ]
        # Return an empty list if no metadata is found
        return []

class ActionArtificialDelay(Action):
    def name(self) -> str:
        return "action_artificial_delay"
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: dict) -> list:
        time.sleep(2)
        return []


def _time_24_to_12(hh_mm: str) -> str:
    """Convert '08:00' -> '8am', '20:00' -> '8pm'."""
    h, m = map(int, hh_mm.split(":"))
    if h == 0:
        return f"12:{m:02d}am" if m else "12am"
    if h < 12:
        return f"{h}{':' + f'{m:02d}' if m else ''}am".rstrip(":")
    if h == 12:
        return f"12{':' + f'{m:02d}' if m else ''}pm".rstrip(":")
    return f"{h - 12}{':' + f'{m:02d}' if m else ''}pm".rstrip(":")


DAY_ORDER = [
    "monday", "tuesday", "wednesday", "thursday",
    "friday", "saturday", "sunday"
]
DAY_ABBREV = {
    "monday": "Mon", "tuesday": "Tue", "wednesday": "Wed",
    "thursday": "Thu", "friday": "Fri", "saturday": "Sat", "sunday": "Sun"
}
# Map full names and common abbreviations to the key used in store_hours.json
DAY_ALIASES = {
    "monday": "monday", "mon": "monday",
    "tuesday": "tuesday", "tue": "tuesday", "tues": "tuesday",
    "wednesday": "wednesday", "wed": "wednesday",
    "thursday": "thursday", "thu": "thursday", "thur": "thursday", "thurs": "thursday",
    "friday": "friday", "fri": "friday",
    "saturday": "saturday", "sat": "saturday",
    "sunday": "sunday", "sun": "sunday",
}


def _normalize_day_to_key(day_input: str) -> str | None:
    """Normalize user input to a day key (e.g. 'Friday' -> 'friday'). Returns None if no match."""
    if not day_input or not isinstance(day_input, str):
        return None
    key = day_input.strip().lower()
    return DAY_ALIASES.get(key)


def _format_all_hours_message(hours_dict: Dict) -> str:
    """Format all days from JSON into the conversational format."""
    lines = ["Our hours of operation are:"]
    for day in DAY_ORDER:
        entry = hours_dict.get(day, {})
        open_t = entry.get("open", "08:00")
        close_t = entry.get("close", "20:00")
        open_str = _time_24_to_12(open_t).replace(":00", "")
        close_str = _time_24_to_12(close_t).replace(":00", "")
        lines.append(f"{DAY_ABBREV[day]} {open_str} - {close_str}")
    return "\n".join(lines)


def _format_single_day_message(hours_dict: Dict, day_key: str) -> str:
    """Format one day's hours. day_key is e.g. 'friday'."""
    entry = hours_dict.get(day_key, {})
    open_t = entry.get("open", "08:00")
    close_t = entry.get("close", "20:00")
    open_str = _time_24_to_12(open_t).replace(":00", "")
    close_str = _time_24_to_12(close_t).replace(":00", "")
    day_display = DAY_ABBREV[day_key]
    # Header: "Our hours on Friday are:" (capitalize first letter of day name)
    day_name_cap = day_key.capitalize()
    return f"Our hours on {day_name_cap} are:\n{day_display} {open_str} - {close_str}"


class ActionGetStoreHours(Action):
    """Load store hours from data/store_hours.json. Supports all hours or a single day via slot_store_hours_day."""
    def name(self) -> str:
        return "action_get_store_hours"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: dict) -> list:
        data_path = Path(__file__).resolve().parent.parent / "data" / "store_hours.json"
        requested_day = tracker.get_slot("slot_store_hours_day")

        try:
            with open(data_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            hours = data.get("hours", {})

            show_all = not requested_day or (isinstance(requested_day, str) and requested_day.strip().lower() == "all")
            if show_all:
                message = _format_all_hours_message(hours)
            else:
                day_key = _normalize_day_to_key(requested_day)
                if day_key is None or day_key not in hours:
                    dispatcher.utter_message(
                        text="I didn't recognize that day. You can ask for a specific day, like Friday, or ask for all store hours."
                    )
                    return []
                message = _format_single_day_message(hours, day_key)

            dispatcher.utter_message(text=message)
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            dispatcher.utter_message(
                text="Sorry, I couldn't load our store hours right now. Please call back or check our website."
            )
        return []
