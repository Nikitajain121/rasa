
# from database_connectivity import DataUpdate
# class ActionFirstName(Action):
#                 def name(self) -> Text: 
#                              """Unique identifier of the form"""
#                              return "action_last_name"

#                  def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#                  dispatcher.utter_message(template="utter_last_name") 
#                  return [SlotSet('firstN',tracker.latest_message['text'])]
# class ActionFeedback(Action): 
#                   def name(self) -> Text: 
#                    """Unique identifier of the form""" 
#                                 return "action_feedback"

#                    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#                                   dispatcher.utter_message(template="utter_feedback")   
#                                   return [SlotSet('lastN',tracker.latest_message['text'])]


# class ActionSubmit(Action): 
#                     def name(self) -> Text: 
#                       """Unique identifier of the form""" 
#                                     return "action_submit"

#                      def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
#                                  DataUpdate(tracker.get_slot("firstN"),    
#                                   tracker.get_slot("lastN"),tracker.get_slot("feedback")) 
#                                   dispatcher.utter_message("Thanks for the valuable feedback. ") 
#                                    return []

# class ActionFormInfo(FormAction): 
#                        def name(self) -> Text: 
#                                       """Unique identifier of the form""" 
#                                       return "form_info"

#                         @staticmethod 
#                         def required_slots(tracker: Tracker) -> List[Text]: 
#                          """A list of required slots that the form has to fill""" 
#                                      return ["firstN", "lastN","feedback"] 
#                          def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]: 
#                        """A dictionary to map required slots to - an extracted entity - intent: value pairs - a whole message or a list of them, where a first match will be picked """ 
#                                         return {
#                                         "firstN": [ self.from_entity( entity="firstN",    
#                                          intent="FirstName"), ], 
#                                           "lastN": [self.from_text()], 
#                                            "feedback": [self.from_text()], }
#                            def submit( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> List[Dict]: 
#                              """Define what the form has to do after all required slots are filled""" # utter submit template

#                                             dispatcher.utter_message(template="utter_submit",   
#                                              Fname=tracker.get_slot("firstN"), 
#                                              Lname=tracker.get_slot("lastN"), 
#                                              fdbk=tracker.get_slot("feedback")) 
#                                              return []
# You can also watch here:


# Storing gathered data to MYSQL database
# Now, it’s time to store the gathered data to the database. For that, there is a function which we are calling above in ActionSubmit which will call a function DataUpdate which will be used to store the data to the database and the program to store the data to the database is given below,

# database_connectivity.py

# import mysql.connector
# def DataUpdate(FirstName,LastName,Feedback): 
#               mydb = mysql.connector.connect( host="localhost", user="root",  
#                passwd="root", database="Rasa_feedback") 
#                mycursor = mydb.cursor() 
#                sql='INSERT INTO FeedBack_rasa_date (firstName, lastName, feedback) VALUES ("{0}","{1}", "{2}");'.format(FirstName,LastName,Feedback) 
#                 mycursor.execute(sql) 
#                 mydb.commit()
