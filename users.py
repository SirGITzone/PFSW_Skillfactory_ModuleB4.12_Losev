import sqlalchemy as sa
from sqlalchemy import Column as Col
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):
    """
    Описывает структуру таблицы user, содержащую данные о них
    """
    __tablename__ = 'user'

    id = Col(sa.Integer, primary_key=True)
    first_name = Col(sa.Text)
    last_name = Col(sa.Text)
    gender = Col(sa.Text)
    email = Col(sa.Text)
    birthdate = Col(sa.Text)
    height = Col(sa.Float)

def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет, и возвращает объект сессии
    """

    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    print("Привет! Давай зафиксируем информацию о тебе!")
    first_name = input("Твоё имя: ")
    last_name = input("Твоя фамилия: ")
    gender = input("Твой пол? (Male или Female) ")
    email = input("Введи Email адрес: ")
    birthdate = input("Введи свою дату рождения в формате ГГГГ-ММ-ДД. Например, 2010-12-19: ")
    height = input("Каков твой рост в метрах? (С помощью точки раздели целую и десятичную часть)")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user

def main():
    """
    Функция для обработки пользовательского ввода
    """
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Данные сохранены. Благодарим за уделённое время!")

if __name__ == "__main__":
    main()
