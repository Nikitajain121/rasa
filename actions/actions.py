# version: "3.1"
# from .database_connectivity import DataUpdate
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher
# import os
# import yaml
# from rasa_sdk.events import UserUtteranceReverted

# from .config import settings

# import os
# #from dotenv import load_dotenv
# import openai


# # Load environment variables from .env file
# print("))))))))))")
# #load_dotenv()
# print("##############")

# print("Ok lets get API KEY")
# api_key = os.getenv("OPENAI_API_KEY")

# # Initialize the OpenAI client with the API key
# openai.api_key = api_key

# print("Hey i got the key!")

# client = openai
# class ActionGetUserName(Action):
#   def name(self) -> Text:
#     return "action_get_user_name"

#   def run(self, dispatcher: CollectingDispatcher,
#           tracker: Tracker,
#           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#     name = next(tracker.get_latest_entity_values("name"), None)
#     if name:
#       # Update slot directly (optional)
#       slot_values = [SlotSet("name", name)]
#       dispatcher.utter_message(f"The user name is set to {name}")
#       DataUpdate(tracker.get_slot("name"))
#       # Update database with error handling
#       try:
#           DataUpdate(name)
#           #print(f"The user name {user_name} fed into the database")
#           dispatcher.utter_message(f"The user name {name} is stored successfully")
#       except Exception as e:
#           print(f"Error updating database: {e}")
#           dispatcher.utter_message("There was an error saving your name. Please try again.")

#       return slot_values
#     else:
#       # Prompt user if no name is extracted
#       dispatcher.utter_message("What is your name?")
#       return []

# # Initialize OpenAI client with your API key

# #client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# GPT_MODEL = "gpt-3.5-turbo-0125"

# class ActionHandleOutOfContext(Action):
#     def name(self) -> Text:
#        # print("2222222222222222")
#         return "action_handle_out_of_context"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Get the user's message
#         user_message = tracker.latest_message.get('text')

#         # Define the conversation message format
#         messages = [
#             {"role": "system", "content": 'You answer question about given data'},
#             {"role": "user", "content": user_message},
#         ]

#         # Call OpenAI API to generate a response
#         response = client.chat.completions.create(
#             model=GPT_MODEL,
#             messages=messages,
#             temperature=0
#         )

#         # Get the generated response
#         #print("333333333333")
#         #generated_response = response.choices[0].message.content
#         #print(response.choices[0])
#         #print( response.choices[0].message.content)
#         # Send the response back to the user
#         #dispatcher.utter_message(text=generated_response)
#         generated_response = response.choices[0].message.content

#         # Send the response back to the user
#         dispatcher.utter_message(text=generated_response)

#         return []

# # Rest of the code remains the same

