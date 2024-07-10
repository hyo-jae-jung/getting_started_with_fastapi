import uvicorn 
from fastapi import FastAPI 
import sys 
sys.path.append('/mnt/d/hyojaejung/workspace/Mywork/getting_started_with_fastapi/part3/web')
import explorer
import creature

app = FastAPI()

@app.get("/")
def top():
    return "top here"

@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"

app.include_router(explorer.router)
app.include_router(creature.router)

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)
