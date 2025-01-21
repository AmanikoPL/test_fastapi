# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# class Item(BaseModel):
#     id: int
#     name: str
#     description: str
#     price: float
#     in_stock: bool

# # Пример данных, которые будут возвращаться
# items = [
#     Item(id=1, name="Laptop", description="A powerful laptop for work and play", price=1200.50, in_stock=True),
#     Item(id=2, name="Smartphone", description="A smartphone with an excellent camera", price=800.99, in_stock=True),
#     Item(id=3, name="Headphones", description="Noise-cancelling over-ear headphones", price=150.75, in_stock=False),
# ]

# @app.get("/items", response_model=list[Item])
# async def get_items():
#     """
#     Возвращает список всех товаров.
#     """
#     return items

# @app.get("/items/{item_id}", response_model=Item)
# async def get_item(item_id: int):
#     """
#     Возвращает конкретный товар по его ID.
#     """
#     for item in items:
#         if item.id == item_id:
#             return item
#     return {"error": "Item not found"}

здесь оставить только запуск uvicorn

if __name__ == "__main__":
    # uvicorn. ваш ip адрес
