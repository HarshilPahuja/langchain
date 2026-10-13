from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

json_schema = {
    "title": "student",
    "description": "Schema about students",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "age": {
            "type": "integer"
        }
    },
    "required": ["name"]
}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""
Extract the student's information from the following text.

Return:
- name: the name of the person who wrote the review
- age: their age, if mentioned

Text:

I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
- Insanely powerful processor
- Stunning 200MP camera
- Long battery life with fast charging
- S-Pen support

Review by Nitish Singh
""")

print(result)


#here  error if not the designed structured output doesnt happen (not always, sometimes can)
# so basically sometimes it happens sometimes it doesnt not sure. depends on method we using and model and langchain version