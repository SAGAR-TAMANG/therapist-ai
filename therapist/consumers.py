from channels.generic.websocket import WebsocketConsumer
import json
from django.template.loader import render_to_string
import uuid

from dotenv import load_dotenv
import os
load_dotenv()

class ChatConsumerDemo(WebsocketConsumer):
  def connect(self):
    self.user = self.scope['user']
    self.messages = [
      {
        "role": "assistant",
        "content": "You are a professional therapist and your name is Pi, and you will take on your client a full therapy session from start to finish. You will act like a real therapist, showing listening skills and acting how a good therapist would.\n \nRemember user's answers and act like a real therapist by trying to understand the user.\n \nBegin by greeting and welcoming, starting with a small talk."
      },
    ]
    self.accept()

  def disconnect(self, code):
    pass
  
  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message_text = text_data_json["message"]

    if not message_text.strip():
      return
    
    # print("Message:", message_text)
    
    # Show users message
    user_message_html = render_to_string(
      "chat/user_msg.html",
      {
        "message_text": message_text,
      },
    )

    # Adding message to history

    self.messages.append(
      {
        "role": "user",
        "content": message_text
      }
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
    
    from portkey_ai import Portkey

    client = Portkey(
      api_key=os.getenv("PORTKEY_API_KEY"),
      virtual_key=os.getenv("VIRTUAL_KEY"),
    )

    stream_prompt_completion = client.chat.completions.create(
      messages=self.messages,
      model= 'gemini-pro',
      stream=True
    )
    
    chunks = []
      
    
    for chunk in stream_prompt_completion:
      # print(chunk.choices[0].delta['content'])
      message_chunk = chunk.choices[0].delta.content
      if message_chunk:
        chunks.append(message_chunk)
        chunk = f'<div hx-swap-oob="beforeend:#{contents_div_id}">{_format_token(message_chunk)}</div>'
        self.send(text_data=chunk)

    system_message = ''.join(chunks)

    final_message_html = render_to_string(
      'chat/ai_msg_final.html',
      {
        'contents_div_id': contents_div_id,
        'message': system_message,
      },
    )

    # Save message

    self.messages.append(
      {
        "role": "system",
        "content": system_message,
      }
    )

    print("TOTAL:", self.messages)

    self.send(text_data=final_message_html)

def _format_token(token: str) -> str:
  # apply very basic formatting while we're rendering tokens in real-time
  token = token.replace("\n", "<br>")
  return token