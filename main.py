from fastapi import FastAPI

app= FastAPI() 
@app.get("/")
def read_root():
    return {'data':{"Hello": "World"}}

@app.get('/about')
def about():
    return {'data':{"About": "This is a simple FastAPI application"}}