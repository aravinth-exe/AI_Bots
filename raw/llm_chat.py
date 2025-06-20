from langchain_ollama import OllamaLLM
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

chat_history = InMemoryChatMessageHistory()
language = 'EN'
chat_history.add_message(SystemMessage(content=f"give result in {language}"))

llm = OllamaLLM(model="deepseek-r1")
user_input = 'coffee'
chat_history.add_user_message(user_input)

message = chat_history.messages

response = llm.invoke(message)
chat_history.add_ai_message(response)

print(chat_history)