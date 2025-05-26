from app.routers import items, database
from fastapi import FastAPI
from app.database_setup import create_db_and_tables


description = """
Welcome to the Learning process API! 🚀

This API provides a comprehensive set of functionalities for managing your e-commerce platform.

Key features include:

- **Crud**
	- Create, Read, Update, and Delete endpoints.


For any inquiries, please contact:

* Github: https://github.com/parulian1
"""


app = FastAPI(
    description=description,
    title="My Learning process API",
    version="1.0.0",
    contact={
        "name": "Martogi Parulian",
        "url": "https://github.com/parulian1",
    },
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai",
        "layout": "BaseLayout",
        "filter": True,
        "tryItOutEnabled": True,
        "onComplete": "Ok"
    },
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(items.router)
app.include_router(database.router)