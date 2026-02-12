from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

history = ["system : you are a helpful friend."]

while True:
    inp = input("You :")
    history.append("User : "+inp)

    response = model.invoke(history)
    history.append("AI : "+ response.content)

    print(history[-1])