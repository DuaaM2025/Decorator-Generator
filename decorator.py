from fastapi import FastAPI
import functools
import time


url = FastAPI()
def log(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        response = await func(*args, **kwargs)
        duration = time.time() - start
        print(f"Endpoint '{func.__name__}' executed in {duration:.4f} seconds")
        return response
    return wrapper

@url.get("/")
@log
async def welcome():
    return {"message": "Welcome, FastAPI"}

