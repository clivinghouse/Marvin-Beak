
import openai
class chat: openai.api_key = "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"

models = openai.Model.list()
def resp(msg):
  chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": msg}])
  chatString = ""
  for choices in chat_completion.choices:
    chatString += choices.message.content;
  return chatString

# print the chat completion
#print(chat_completion.choices[0].message.content)