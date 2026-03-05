from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("AIzaSyDh1EvBEkzI7QEZ-0yG4inu-6pwFljc5YU"))

response = client.chat. completions. create(
model="gpt-4o-mini",
messages=[{"role":"user","content":"Say Hello Kitchen Vision"}]

)


print(response. choices[0].message.content)