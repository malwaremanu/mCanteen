import os
from fastapi import FastAPI, Request
from deta import Deta

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=['*']
)

from deta import Deta
from dotenv import load_dotenv
load_dotenv()

#deta = Deta("c0qm30mo_ZAEx1mTufH9EyGpDivRP3p56x1PxoqzY")
deta = Deta(os.getenv('deta_key'))


#app = Flask(__name__)
from users.users import router as users_router
app.include_router(users_router)


products = deta.Base("products")

# Delete working
@app.delete('/products/{id}')
async def deleteProducts(id:str):
    products.delete(id)
    return {
        "status" : "SUCCESS",
        "message":f"user with id {id} deleted"
    }


# Update working
@app.put('/products/{id}')
async def updateProducts(id:str, request : Request):
    try:
        r = await request.json()
        print(r.get('empno'))    
        products.put({"user":r},id)
        #return {"message":f"user with id {id} updated"}
        return {
            "status" : "SUCCESS",
            "message":f"user with id {id} updated",
            "data" : r
        }
    except:
        return {
            "status" : "ERROR",
            "message":f"user with id {id} was not updated",
        }


@app.post('/products/')
async def postProducts(request : Request):
    # id:str and user: str implies input validation, ie the url parameters can be of only type string
    r = await request.json()
    products.insert({"product":r})
    return {
        "status" : "SUCCESS",
        "message" : "User created successfully",
        "data" : r
    }


@app.get('/products/')
async def getProducts():
    respose={}
    # fetches all the users from Deta cloud db
    allproducts=products.fetch()
    for item in allproducts.items:
        respose[item["key"]]=item["product"]
    return respose
    