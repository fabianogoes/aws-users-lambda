import jwt
import os
from dotenv import load_dotenv
from jwt.exceptions import ExpiredSignatureError

load_dotenv()
SECRET = os.getenv("SECRET")

class User: 
    def __init__(self, cpf, name, email): 
        self.cpf = cpf 
        self.name = name 
        self.email = email

database = [
    User("12345678901", "Fulano", "fulano@gmail.com"),
    User("10987654321", "Ciclano", "ciclano@hotmail.com"),
    User("11133344455", "Beltrano", "beltrano@gmail.com"),
    User("11111111111", "Teste", "test@test.com"),
    User("99999999999", "Fabiano", "fabiano@gmail.com")
]

def lambda_handler(event, context):
    print("*********** Users Pool the event is: *************")
    print(event)

    data = event['cpf']
    user = None
    for u in database:
        if u.cpf == data:
            user = u
            break

    if user is None:
        return {
            'statusCode': 404,
            'body': 'User not found'
        }

    return {
        'statusCode': 200,
        'body': user.__dict__
    }
   

if __name__ == '__main__':
    print("--- Running locally ---")
    context = None
    event = {
        'cpf': '11133344456'
    }

    print(lambda_handler(event, context))
