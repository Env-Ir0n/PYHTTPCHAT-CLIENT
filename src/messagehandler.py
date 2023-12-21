import requests
import src.jsonhandler as json
import src.encryptionservice as PGP

def getmsg(serverip,authkey,publickey):
    headers = {
        'Auth':authkey,
        'Encrypted?':'True',
        'PGP:':publickey
    }
    response = requests.get(f'{serverip}/messages',headers=headers)
    if response.status_code == 200:
        print('Got messages!')
        msg = json.loads(response.content)
        msgs = PGP.decrypt(msg,publickey)
        return msgs
    elif response.status_code == 401:
        return 401
    else:
        return response.status_code

    


def send(serverip,authkey,publickey,message):
    
    
    JSON = json.retrieve('client.json')
    user = JSON['username']
    headers = {
        'Content-type':'text/html',
        'Auth':authkey,
        'Encrypted?':'False',
        'PGP:':publickey,
        'username':user
    }
    content = PGP.encrypt(message,publickey)
    response = requests.post(f'{serverip}/messages/send',content,headers=headers)
    if response.status_code == 200:
        print('SENT!')
        input('Continue > ')

    elif response.status_code == 401:
        print('401:')
        print(response.content)
        input('continue > ')
        return 401
    
    else:
        print(f'{response.status_code}:')
        print(response.content)
        input('continue > ')
        getmsg(serverip,authkey,publickey)
        return response.status_code
    
    
def INIT(serverip,password,publickey):
    headers = {
        'Password':password,
        'Encrypted?':'False',
        'PGP:':publickey
    }
    response = requests.get(f'{serverip}/init', headers=headers)

    if response.status_code == 200:
        print('Authkey got!')
        return response.headers['Auth']
    elif response.status_code == 401:
        return 401
    else:
        return response.status_code
        
def INFO(serverip,authkey,publickey):
    headers = {
        'Auth':authkey,
        'Encrypted':'False',
        'PGP:':publickey
    }

    response = requests.get(serverip,headers=headers)

    if response.status_code == 200:
        return 200, response.content
    else:
        return response.status_code
        
def banish(authkey,serverip):
    headers = {
        'Auth':authkey
    }
    requests.get(f'{serverip}/banish',headers=headers)
    