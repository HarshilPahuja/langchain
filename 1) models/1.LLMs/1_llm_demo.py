from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #auto loads api key cause we mentioned it in a standard way of OPENAI_API_KEY
# else need to pass explicitly like
#import os

# llm = OpenAI(
#     model="gpt-3.5-turbo-instruct",
#     api_key=os.getenv("OPENAI_API_KEY")
# )
llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")

print(result)