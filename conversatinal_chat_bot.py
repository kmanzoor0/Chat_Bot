from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model = 'llama-3.1-8b-instant',temperature = 0.8)

chat_history = []
prompt = ChatPromptTemplate.from_messages([
    ('system','You are a helpful ChatBot'),
    MessagesPlaceholder(variable_name = "chat_history"),
    ('human','{question}')
])
parser = StrOutputParser()
chain = prompt|model|parser
while True:
    user_input = input('Ask Something :').strip().lower()
    if user_input == 'exit':
        print("""'Bot' : 'GoodBye'""")
        break
    result= chain.invoke({'chat_history':chat_history,'question':user_input})
    print('Bot:',result)

    chat_history.append(HumanMessage(content = user_input))
    chat_history.append(AIMessage(content = result))