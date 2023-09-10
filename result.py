import os
from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

token = os.environ['COOKIE_TOKEN']
bard = Bard(token=token)

def get_answer(question):
  response = bard.get_answer(question)
  return response['content']

if __name__ == '__main__':
  question = input('Where is Riga Technical University: ')
  answer = get_answer(question)
  print(answer)
