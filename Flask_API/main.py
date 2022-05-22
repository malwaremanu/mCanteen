import os
from fastapi import FastAPI, Request
from deta import Deta

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=['*']
)

#app = Flask(__name__)
from users.users import router as users_router
from products.products import router as products_router
from categories.categories import router as categories_router

app.include_router(users_router)
app.include_router(products_router)
app.include_router(categories_router)

# from deta import Deta
# from dotenv import load_dotenv
# load_dotenv()

# #deta = Deta("c0qm30mo_ZAEx1mTufH9EyGpDivRP3p56x1PxoqzY")
# deta = Deta(os.getenv('deta_key'))

# products = deta.Base("products")

