from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser  # model returns content - json and other metadata. 
#when we do model.invoke template it returns result , result has content and other meta data. we do result.content and send that to parser But in chain we directly sent entire result to parser
#cuz parser correctly extract content itself.
result = chain.invoke({'topic':'black hole'}) 
#note everytime u do chain.invoke({u need to send a dictionary here})
#if no input variable send empty dictionary else send the input variable in dictionary.

print(result)



