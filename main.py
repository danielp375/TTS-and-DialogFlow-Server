from flask import Flask, request, send_file
from test_model import process_message
from dialogflow_demo import process_chat
from settings import OUTPUT_FILE

app = Flask(__name__)

@app.route('/message', methods = ["POST"])
def send_message():
    
    data = request.get_json()

    ### takes message - str
    message = data["message"]
    
    ### process message
    file_name = process_message(message=message)
    
    ### return audio file
    return send_file(
       file_name, 
       mimetype="audio/wav", 
       as_attachment=True
    )
    
@app.route('/chat', methods = ["POST"])
def send_chat():
    
    data = request.get_json()

    ### takes message - str
    message = data["message"]
    
    ### process message
    chat_msg = process_chat(chat=message)
    
    ### return audio file
    return chat_msg


if __name__ == "__main__":
    app.run(debug = True, host = "127.0.0.1", port = 5000)