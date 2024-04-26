# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# # from typing import Any, Text, Dict, List
# #
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# #
# #
# # class ActionHelloWorld(Action):
# #
# #     def name(self) -> Text:
# #         return "action_hello_world"
# #
# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #         dispatcher.utter_message(text="Hello World!")
# #
# #         return []
# from .database_connectivity import DataUpdate

# from typing import Any, Text, Dict, List
# #from translate import Translator
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher

# class ActionGetUserName(Action):
#     def name(self) -> Text:
#         return "action_get_user_name"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         user_name = next(tracker.get_latest_entity_values("user_name"), None)
#         if user_name:
#             slot_values = [SlotSet("user_name", user_name)]
#             # Send a message confirming the slot value
#             dispatcher.utter_message(f"The user name is set to {user_name}")
#             print("un 1",user_name)
#             DataUpdate(user_name)
#             print("un 2",user_name)
#             dispatcher.utter_message(f"The user name feed in databse to {user_name}" )
#             print("un 3",user_name)
#             return slot_values

#         return []
    
from .database_connectivity import DataUpdate
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionGetUserName(Action):
  def name(self) -> Text:
    return "action_get_user_name"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    user_name = next(tracker.get_latest_entity_values("user_name"), None)
    if user_name:
      # Update slot directly (optional)
      slot_values = [SlotSet("user_name", user_name)]
      dispatcher.utter_message(f"The user name is set to {user_name}")
      DataUpdate(tracker.get_slot("user_name"))
      # Update database with error handling
      try:
          DataUpdate(user_name)
          #print(f"The user name {user_name} fed into the database")
          dispatcher.utter_message(f"The user name {user_name} is stored successfully")
      except Exception as e:
          print(f"Error updating database: {e}")
          dispatcher.utter_message("There was an error saving your name. Please try again.")

      return slot_values
    else:
      # Prompt user if no name is extracted
      dispatcher.utter_message("What is your name?")
      return []
