from fastapi import FastAPI

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