from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Базовый класс для моделей
Base = declarative_base()

# Модель "Рецепт"
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор
    name = Column(String, nullable=False)  # Название рецепта
    ingredient_one = Column(String, nullable=False)  # Первый ингредиент
    ingredient_two = Column(String, nullable=False)  # Второй ингредиент

    def __repr__(self):
        return f"<Recipe(name='{self.name}', ingredient_one='{self.ingredient_one}', ingredient_two='{self.ingredient_two}')>"
