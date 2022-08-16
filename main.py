
from fastapi import FastAPI


server = FastAPI()

  

@server.get('/')
def get_reply():
  return 'Hellow world!'
      

     
