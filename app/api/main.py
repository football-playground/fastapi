import uvicorn
from fastapi import FastAPI
from routers.england import router_en
from routers.france import router_fr
from routers.germany import router_ge
from routers.italy import router_it
from routers.spain import router_sp

app = FastAPI()
app.include_router(router_en)
app.include_router(router_fr)
app.include_router(router_ge)
app.include_router(router_it)
app.include_router(router_sp)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)