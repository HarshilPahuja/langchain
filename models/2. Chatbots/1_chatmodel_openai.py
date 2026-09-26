from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)

#in LLM we get only text output
#in chatmodel

# content='The capital of India is New Delhi.'
# additional_kwargs={'refusal': None}  //modal didnt refuse to answer.
# response_metadata={
#     'token_usage': {
#         'completion_tokens': 9, //model output token
#         'prompt_tokens': 14,  //our token
#         'total_tokens': 23,
#         'completion_tokens_details': {
#             'accepted_prediction_tokens': 0,
#             'audio_tokens': 0,
#             'reasoning_tokens': 0,
#             'rejected_prediction_tokens': 0
#         },
#         'prompt_tokens_details': {
#             'audio_tokens': 0,
#             'cached_tokens': 0
#         }
#     },
#     'model_name': 'gpt-4-0613',
#     'system_fingerprint': None,
#     'finish_reason': 'stop', //finished normally, didnt hit token limit or anything
#     'logprobs': None
# }
# id='run-50960ad6-1055-4ae0-8a70-71e0b47ee4b4-0'
# usage_metadata={
#     'input_tokens': 14,
#     'output_tokens': 9,
#     'total_tokens': 23,
#     'input_token_details': {
#         'audio': 0,
#         'cache_read': 0
#     },
#     'output_token_details': {
#         'audio': 0,
#         'reasoning': 0
#     }
# }
# ```




# Temperature is a parameter that controls the randomness of a language model's output. It affects
# how creative or deterministic the responses are.

# • Lower values (0.0 - 0.3) → More deterministic and predictable.
# • Higher values (0.7 - 1.5) → More random, creative, and diverse.


# | Use Case                              | Recommended Temperature |
# |---------------------------------------|-------------------------|
# | Factual answers (math, code, facts)  | 0.0 - 0.3              |
# | Balanced response (general QA, explanations) | 0.5 - 0.7       |
# | Creative writing, storytelling, jokes | 0.9 - 1.2             |
# | Maximum randomness (wild ideas, brainstorming) | 1.5+            |

