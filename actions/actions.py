import os
import time
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


class ActionGetStoreHours(Action):
    """Simple custom action that returns store hours."""
    def name(self) -> str:
        return "action_get_store_hours"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: dict) -> list:
        dispatcher.utter_message(
            text="Our store hours are 9 AM to 6 PM, Monday through Saturday. We're closed on Sundays."
        )
        return []
