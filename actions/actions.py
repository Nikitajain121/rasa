from .database_connectivity import DataUpdate
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import os
import yaml
from rasa_sdk.events import UserUtteranceReverted
from openai import OpenAI

# Initialize OpenAI client with your API key
client = OpenAI(api_key=${{secrets.OPENAI_KEY}})
GPT_MODEL = "gpt-4" #"gpt-3.5-turbo-1106"

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

