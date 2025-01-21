import hashlib
from ....models import Recipe
# SHA256


def login:
    считываем из pydantic модели json юзера

    pydantic стучится в БД и проверяет есть ли такой логин с юзером
    если он есть проверяем пароль а его хэш
    если хэши совпадают, то формируем Json Webtoken JWT отправяем его в ответе клиенту

    JWT - шифр, в котором шифруются данные юзера
    вы можете туда положить все что угодно про юзера
    например его имя, срок действия

    python jose
    jose - python 2

    # token = jose
    # token lifetime

    return token 


def register:
    

def reset_password:
    


перед отправкой данного запроса прикрепляете заголовок Authorization: Bearer JWT

http://localhost:8000/auth/profile

headers:
Authorization: Bearer asnsfjksndfkjsdnfjksddnfjsdnfksdnfkjsdnfsdnfksjdn
def get_user_profile:
