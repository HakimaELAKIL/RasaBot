# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBookFlight(Action):
    def name(self):
        return "action_book_flight"

    def run(self, dispatcher, tracker, domain):
        ville_depart = tracker.get_slot("ville_depart")
        ville_destination = tracker.get_slot("ville_destination")
        date_depart = tracker.get_slot("date_depart")
        date_retour = tracker.get_slot("date_retour")
        classe = tracker.get_slot("classe")
        type_vol = tracker.get_slot("type")

        message = f"وجدنا رحلة من {ville_depart} إلى {ville_destination} يوم {date_depart}"
        if type_vol == "aller-retour" and date_retour:
            message += f" والعودة يوم {date_retour}"
        if classe:
            message += f" في درجة {classe}"
        message += ". هل تريد تأكيد الحجز؟"

        dispatcher.utter_message(text=message)
        return []

class ActionBookHotel(Action):
    def name(self):
        return "action_book_hotel"

    def run(self, dispatcher, tracker, domain):
        ville = tracker.get_slot("ville")
        quartier = tracker.get_slot("quartier")
        categorie = tracker.get_slot("catégorie")
        personnes = tracker.get_slot("nombre_personnes")

        message = f"يوجد فندق {categorie} نجوم في {ville}"
        if quartier:
            message += f"، حي {quartier}"
        if personnes:
            message += f"، لشخص {personnes}"
        message += ". هل تريد تأكيد الحجز؟"

        dispatcher.utter_message(text=message)
        return []

class ActionConfirm(Action):
    def name(self):
        return "action_confirm"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(response="utter_confirm")
        return []

class ActionChangeOption(Action):
    def name(self):
        return "action_change_option"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(response="utter_change")
        return []