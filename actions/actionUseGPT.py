import os
from dotenv import load_dotenv
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

class ActionUseGPT(Action):
    def name(self):
        return "action_use_gpt"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get('text')
        response  = self.get_gpt_response(user_message)
        dispatcher.utter_message(text=response)
        return []
    
    def get_gpt_response(self, prompt):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content