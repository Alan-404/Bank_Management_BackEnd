import jwt

from random import randrange, randint


from common.constants import Constants


def getIdByToken(request):
    header = request.headers.get('Authorization')
    token = header.split()[1];
    decoded = jwt.decode(token, Constants.my_token_key, algorithms="HS256")
    return decoded["id"]

def makeAccessToken(account):
    payload = {
            "id": account.id
        }

    return jwt.encode(payload, Constants.my_token_key, algorithm="HS256")


def makeIdCard():
    bin = "1234"
    card = bin
    for i in range(12):
        if i%4 == 0:
            card += " "
        card += str(randrange(10))  
        
    return card

def makeId():
    id = ""
    for i in range(10):
        id+= str(randint(0,9))
    return id


