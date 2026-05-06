from agno.models.groq import Groq
from agno.models.message import Message
from dotenv import load_dotenv
load_dotenv()

model = Groq(id="llama-3.3-70b-versatile")
msg = Message(
    role="user",
    content=[{"type": "text", "text": "Olá, Meu nome é Alexandre"}]
)
response = model.response([msg])

response.content