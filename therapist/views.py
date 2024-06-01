from django.shortcuts import render, HttpResponse
from dotenv import load_dotenv
import os
load_dotenv()

def index(request):
  return render(request, 'index.html')

def app(request):
  return render(request, 'app.html')

def ai(request):
  from portkey_ai import Portkey

  client = Portkey(
    api_key=os.getenv("PORTKEY_API_KEY"),
    virtual_key=os.getenv("VIRTUAL_KEY"),
  )

  # completion = client.chat.completions.create(
  # prompt_id="pp-ai-therapi-f9b710",
  # variables={}
  # )

  stream_prompt_completion = client.prompts.completions.create(
    prompt_id="pp-ai-therapi-f9b710",
    variables={},
    stream=True
  )

  # Access and handle the response stream using the _iterator attribute
  response_text = ""
  
  for chunk in stream_prompt_completion._iterator:
      # Process each chunk of data here
      # Assuming the chunk is an instance of PromptCompletionChunk
      print(chunk)
      
      # Check if the chunk has a 'text' attribute
      if hasattr(chunk, 'text'):
          response_text += chunk.text
      else:
          # If 'text' attribute is not present, try accessing other potential attributes or methods
          # Adjust this based on the actual structure of PromptCompletionChunk
          if hasattr(chunk, 'data'):
              response_text += chunk.data
          elif hasattr(chunk, 'get_text'):
              response_text += chunk.get_text()
          else:
              response_text += str(chunk)  # Convert to string if no suitable attribute or method is found

  print('\n\nFINAL \n\n')

  print("Complete response:", response_text)
  
  return render(request, 'app.html')