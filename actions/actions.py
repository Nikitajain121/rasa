from .database_connectivity import DataUpdate
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher 
from rasa_sdk.forms import FormValidationAction 
from rasa_sdk.events import EventType 

import os
import yaml
from rasa_sdk.events import UserUtteranceReverted
from openai import OpenAI

#from dotenv import load_dotenv
#load_dotenv()
### HWHHUW
#openai.api_key= os.environ.get('OPENAI_API_KEY')

OPENAI_API_KEY= ${{ secrets.OPENAI_API_KEY }}
client = OpenAI(api_key=OPENAI_API_KEY)
# Initialize OpenAI client with your API key

GPT_MODEL = "gpt-3.5-turbo-1106"

class ActionHandleOutOfContext(Action):
    def name(self) -> Text:
        print("2222222222222222")
        return "action_handle_out_of_context"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the user's message
        user_message = tracker.latest_message.get('text')

        # Define the conversation message format
        messages = [
            {"role": "system", "content": 'You answer question about given data'},
            {"role": "user", "content": user_message},
        ]

        # Call OpenAI API to generate a response
        response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=messages,
            temperature=0
        )

        # Get the generated response
        print("333333333333")
        #generated_response = response.choices[0].message.content
        #print(response.choices[0])
        #print( response.choices[0].message.content)
        # Send the response back to the user
        #dispatcher.utter_message(text=generated_response)
        generated_response = response.choices[0].message.content

        # Send the response back to the user
        dispatcher.utter_message(text=generated_response)

        return []

# Rest of the code remains the same

class FormDataCollect(FormValidationAction):
    def name(self) -> Text:
        return "Form_Info"
    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["user_name","phone"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return {
        #"name":[self.from_text(entity="name")],
        "phone":[self.from_entity(entity="phone")],
        "user_name":[self.from_entity(entity="user_name")]
        }

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        dispatcher.utter_message("Here are the information that you provided. Do you want to save it?\nName: {0},\nMobile Number: {1}".format(
        #tracker.get_slot("name"),
        tracker.get_slot("user_name"),
        tracker.get_slot("phone")
        ))
        return []
# class ActionGetUserName(Action):
# #   def name(self) -> Text:
# #     return "action_get_user_name"

#   def run(self, dispatcher: CollectingDispatcher,
#           tracker: Tracker,
#           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#     #user_name = next(tracker.get_latest_entity_values("user_name"), None)
#     # user_name = tracker.get_slot("user_name")
#     # phone = tracker.get_slot("phone")
#     # if user_name:
#     #   # Update slot directly (optional)
#     #   slot_values = [SlotSet("user_name", user_name)]
#     #   dispatcher.utter_message(f"The user name is set to {user_name}")
#     DataUpdate(tracker.get_slot("user_name"),tracker.get_slot("phone"))
#       # Update database with error handling
    #   try:
    #       DataUpdate(user_name)
    #       #print(f"The user name {user_name} fed into the database")
    #       dispatcher.utter_message(f"The user name {user_name} is stored successfully")
    #   except Exception as e:
    #       print(f"Error updating database: {e}")
    #       dispatcher.utter_message("There was an error saving your name. Please try again.")

    #   return slot_values
    # else:
    #   # Prompt user if no name is extracted
    #   dispatcher.utter_message("What is your name?")
    #   return []
# class ActionGetUserName(Action):
#     def name(self) -> Text:
#         return "action_get_user_name"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         user_name = tracker.get_slot("user_name")
#         phone = tracker.get_slot("phone")

#         if user_name and phone:
#             DataUpdate(user_name, phone)
#             dispatcher.utter_message(f"The user name {user_name} and phone number {phone} are stored successfully")
#         else:
#             if not user_name:
#                 dispatcher.utter_message("Please provide your name.")
#             if not phone:
#                 dispatcher.utter_message("Please provide your phone number.")

#         return []
class ActionSaveData(Action):
    def name(self) -> Text:
        return "action_save_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        DataUpdate(tracker.get_slot("user_name"),tracker.get_slot("phone"))
        dispatcher.utter_message(text="Data Stored Successfully.")
        return []
