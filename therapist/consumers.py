from channels.generic.websocket import WebsocketConsumer
import json
from django.template.loader import render_to_string
import uuid

class ChatConsumerDemo(WebsocketConsumer):
  def connect(self):
    self.accept()

  def disconnect(self, code):
    pass
  
  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message_text = text_data_json["message"]

    if not message_text.strip():
      return
    
    print("Message:", message_text)
    
    # Show users message
    user_message_html = render_to_string(
      "chat/user_msg.html",
      {
        "message_text": message_text,
      },
    )

    self.send(text_data=user_message_html)

    # render an empty text 

    message_id = uuid.uuid4().hex
    contents_div_id = f"message-response-{message_id}"
    system_message_html = render_to_string(
      "chat/ai_msg.html",
      {
        "contents_div_id": contents_div_id,
      },
    )

    self.send(text_data=system_message_html)