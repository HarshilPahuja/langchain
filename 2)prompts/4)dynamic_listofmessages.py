from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    SystemMessage(content='You are a helpful {domain} expert'),
    HumanMessage(content='Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Dusra'})

print(prompt)

#output
# messages=[
#     SystemMessage(
#         content='You are a helpful [domain] expert',
#         additional_kwargs={},
#         response_metadata={}
#     ),
#     HumanMessage(
#         content='Explain in simple terms, what is {topic}',
#         additional_kwargs={},
#         response_metadata={}
#     )
# ]

# the parameters didnt get filled, baaki jagah to horhe the, this is weird behaviour cause not much mature library.

# so need to pass here in a little different way
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)

#need to pass a tuple.



# placeholder
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)