from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')


#no control ki LLM negative/positive hi sirf return krega instead it can return sth else. so need to use pydantic
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2 # classifies if sentiment positive or negative


prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(  #inside this we pass tuples, each tuple (condition, chain) - if condition true execute that chain
#(condition1, chain1),
#(condition2, chain2),
#default chain
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),  #function, with input param as x.
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")  #returns could not find sentiment
    #we simply returning that, and input is x. 
    #kuch processing nhi hai, need to make it a chain. so need to make it a runnable
    #runnablelambda- converts a lambda to runnable. once its runnable can use it in chain.
    #https://chatgpt.com/share/6abe3a95-2a10-83ee-9e5c-1667f54d0e99 
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()