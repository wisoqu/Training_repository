from g4f.client import Client # necessary imports

client = Client() # making class
response = client.chat.completions.create( # creating response
    model="gpt-4.1",  # Choosing models
    messages=[{"role": "user", "content": "Hello"}], # Sending message to model
    web_search=False # Offing search (actual for new models with search modes)
)
print(response.choices[0].message.content) # just showing result
print()

"""
In english for english practice, PyCharm 2025.2.5 version
I got this code from the official documentation:
https://g4f.dev/docs/
"""