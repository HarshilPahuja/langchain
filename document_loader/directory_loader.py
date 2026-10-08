

# if reading all txt files
from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    path='books',
    glob='*.txt',
    loader_cls=TextLoader
)

docs = loader.load()

# if reading pdf
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

#if reading all type of files csv pdf txt can make it like this
pdf_loader = DirectoryLoader(
    "books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

txt_loader = DirectoryLoader(
    "books",
    glob="*.txt",
    loader_cls=TextLoader
)

docs = pdf_loader.load() + txt_loader.load()    




#load.

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()
for document in docs:
    print(document.metadata)

#shuru mei kuch nhi hoga kaafi time tk then sab saara ek saath

#lazy_load
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()
for document in docs:
    print(document.metadata)

#no upfront work and ekdum se stream ki tarak 1-1 print.

