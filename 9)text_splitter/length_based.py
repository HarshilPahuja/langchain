from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load() #5 pages in pdf = 5 document objects here

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0, #tells 2 chunks ke beechme kitne characters ka overlap hoga. #use case:- character splitter abruptly beechme se cuts the word. so to make probaiblity of saving context higher, we use this. starting next chunk thora peeche se.
    # in a rag based application 10-20% of chunk_size is a good number.
    separator='' # no seperator : reached 200 chars we'll split.
)
#https://chunkviz.up.railway.app/

result = splitter.split_documents(docs)

print(result) #list of chunks