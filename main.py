from typing import Optional
from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


@app.get("/") #Decorator (method, path)
def read_root(): #Funtion
    return {"Hello": "Benee!!!"}

@app.get("/months")
def months():
    return {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}


                                        #POST method

class post(BaseModel): 
    id : int
    title : str
    content : str
    published : bool
    rating : Optional[int]


@app.post("/post") #Simple post without validation
def createpost(payload: dict = Body(...)): #converting the payload to a dictionary
    print(payload)
    return{"New post created" : payload}


@app.post("/createpost") #Post with schema validation from pydantic basemodel
def createpost(Post : post):
    #print(Post.dict()) #converting the payload to a dictionary
    return{"New post created" : Post }


userpost = [
    {
        "id" : "1",
        "title" : "First story",
        "content" : "This is my first story"
    },
    {   "id" : "2",
        "title" : "Second story",
        "content" : "This is my second story"
    },
    {
        "id" : "3",
        "title" : "Third story",
        "content" : "This is my third story" 
    }
        ]

@app.get("/userposts")
def getpost():
    return{"data" : userpost}

@app.post("/userposts") #decorator
def createpost(post : post): #defining the payload
    convdict = post.dict()      #converting pydentic model to a dictionary
    convdict["id"] = randrange(0 , 1000000) #generating random id using randrange
    userpost.append(convdict)
    return{"Successful" : convdict}


@app.get("/userposts/{id}")
def getpostbyID():
    return{"data"}
