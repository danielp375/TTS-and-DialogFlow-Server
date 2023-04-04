import os      #importing the OS module for setting up service account credentials in environment
from google.cloud import dialogflow     #importing the dialogflow API
from google.api_core.exceptions import InvalidArgument     #For any GCS exceptions
from settings import PROJECT_ID, CREDENTIALS, LANGUAGE_CODE, SESSION_ID     #importing names

#Storing the service account credentials in Environment
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS

#Setting up Dialogflow details
DIALOGFLOW_PROJECT_ID = PROJECT_ID
DIALOGFLOW_LANGUAGE_CODE = LANGUAGE_CODE
SESSION_ID = SESSION_ID

#Creating a session client
session_client = dialogflow.SessionsClient()
#Creating a session using the session client
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
#Getting the response from Dialogflow
def process_chat(chat):
    text_to_be_analyzed = chat #Request text sent to the chatbot
    #Creating the query to be sent
    text_input = dialogflow.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.QueryInput(text=text_input)
    try:
        #Using the session and query to send a request to Dialogflow
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    #Returning the response
    return response.query_result.fulfillment_text
    