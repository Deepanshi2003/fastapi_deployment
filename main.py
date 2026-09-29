from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def home():
    return{
        "message":'hello dpanshii how are you'
    }