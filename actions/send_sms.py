import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
#from twilio.rest import Client

#####
# Send SMS
class ActionSendSmsPromoText(Action):
    def name(self) -> Text:
        return "action_send_sms_promo_text"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:

        # Get the callee number from slot
        # * e.g. Who is being called
        #caller_number = tracker.get_slot('user_phone')
        #callee_number = "+1XXXXXXXXXX"

        # Twilio credentials
        # * Store these securely in environment variables
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token =  os.environ.get("TWILIO_AUTH_TOKEN")
        twilio_number = "+1 XXX XXX XXXX"

        # Link to send in SMS text
        url = "https://rasa.com"

        try:
            # Send SMS
            # * Initialize Twilio client
            #client = Client(account_sid, auth_token)
            #client.messages.create(
            #    body=f"CSS: Here's the link to your subscription discount: {url}",
            #    from_=twilio_number,
            #    to=caller_number
            #)

            # Send success message to user
            #dispatcher.utter_message(text="I've sent the link to your phone number.")
            pass  # Placeholder for when SMS functionality is enabled

        except Exception as e:
            dispatcher.utter_message(text="Sorry, I was unable to send the SMS link.")

        return []