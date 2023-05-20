
import openai
class chat: openai.api_key = "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"

models = openai.Model.list()
  def resp(msg):
     chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": msg}])
     return chat_completion

# print the chat completion
#print(chat_completion.choices[0].message.content)