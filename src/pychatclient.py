import jsonhandler as json
import messagehandler
import secondinit as initII
import os

if os.path.exists('init.txt'):
    pass
else:
    initII.init()

info = json.retrieve('client.json')
if info['server']['save'] == True:
    e = json.isthere('list',info['server'])
    if e == True:
        recentserverlist = info['server']['list']
    else:
        new = info
        new['server']['list'][1] = 'No servers saved'
        new['server']['list'][2] = 'No servers saved'
        new['server']['list'][3] = 'No servers saved'
        new['server']['list'][4] = 'No servers saved'
        new['server']['list'][5] = 'No servers saved'
        json.commit('client.json',new)
else:
    recentserverlist = None

def newserver(address,password):
    info = json.retrieve('client.json')
    if address in info['server']['auth']:
        global conn
        global authkey
        authkey = info['server']['auth'][address]
        conn = address
        return 'Server is listed'
    else:
        print('Initiating init (^C to cancel)')
        try:
            response = messagehandler.INIT(address,password,publickey=None)
            if isinstance(response, int):
                print(f'error!: {response}')
                return 'ERROR'
            else:
                print('200! got authkey!')
                print(f'AUTHKEY: {response}')
                info['server']['auth'][address] = response
                global authkey
                authkey = response
                global conn
                conn = address
                with open('public.asc') as f:
                    global public
                    public = f.read()
                response = messagehandler.INFO(address,authkey,public)
                info['server']['info'][address]['public'] = response
                json.commit('client.json',info)
                
            
        except KeyboardInterrupt:
            print('Canceled')

if recentserverlist == None:
    address = input('Server address: ')
    password = input('Password (leave blank if none): ')
    newserver(address,password,password)
else:
    info = json.retrieve('')
    one = info['server']['list'][1]
    two = info['server']['list'][2]
    three = info['server']['list'][3]
    four = info['server']['list'][4]
    five = info['server']['list'][5]
    print('saved serverlist')
    print('[0]: connect to a new server')
    print(f'[1]: {one}')
    print(f'[2]: {two}')
    print(f'[3]: {three}')
    print(f'[4]: {four}')
    print(f'[4]: {five}')
    print('Input the number to connect')
    connect_to = input('> ')
    if connect_to == '1':
        newserver(one,None)
    elif connect_to == '2':
        newserver(two,None)
    elif connect_to == '3':
        newserver(three,None)
    elif connect_to == '4':
        newserver(four,None)
    elif connect_to == '5':
        newserver(five,None)
    elif connect_to == '0':
        address = input('Server address: ')
        password = input('server password (leaveblank if none): ')
        newserver(address,password)
    else:
        print('Error, Incorrect statement!')
        quit()

with open('public.asc') as f:
    public = f.read()

messages = messagehandler.getmsg(conn,authkey,public)
for keys in messages:
    msg = messages[keys] 
    user = keys
    print(f'{user} : {msg}')

while True:
    action = input('Action > ')
    if action == '?':
        print('actions:')
        print('send OR -s : begins the sender proccess of a message')
        print('update OR -u : updates messages')
        print('quit : quits the program safely')
    
    elif action == 'send' or '-s':
        try:
            message = input('Message (^C to cancel)')
        except KeyboardInterrupt:
            print('cancelled')
            exit()
        messagehandler.send(address,authkey,public,message)
    
    elif action == 'update' or '-u':
        messages = messagehandler.getmsg(conn,authkey,public)
        for keys in messages:
            msg = messages[keys] 
            user = keys
            print(f'{user} : {msg}')

    elif action == 'quit':
        quit('Quit successfully')

# :3