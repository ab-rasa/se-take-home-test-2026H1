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
