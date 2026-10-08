from langchain_community.document_loaders import TextLoader


loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

# print(docs) #list of documents
# print(docs[0])
# print(type(docs[0])) #document object
print(docs[0].page_content)

#rest loaders also simillar syntax