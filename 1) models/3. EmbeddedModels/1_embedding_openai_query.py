from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))

#output - a 32D vector the vector represents the entire sentence not token level, better for rag instead of token level
#dimensions=hyperparameter


# mostly model dont allow you to input custom dimensions they have fixed, but this is just for demonstration
# Higher dimensions
#       ↓
# More information capacity
#       ↓
# Potentially better retrieval quality
#       ↓
# More storage + memory + computation

# Lower dimensions
#       ↓
# Less storage + faster vector operations
#       ↓
# Potentially some loss in retrieval quality