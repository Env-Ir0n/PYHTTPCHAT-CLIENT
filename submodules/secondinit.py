import jsonhandler as json

def init():
    save = input('Save recent servers in a list? (Y/n)')
    if save == 'Y':
        JSON = json.retrieve('client.json')
        JSON['server']['save'] = True
    else:
        JSON = json.retrieve('client.json')
        JSON['server']['save'] = False

    JSON['serverkeys']['eg'] = '1234'
    json.commit('client.json',JSON)
    with open('init.txt'):
        pass
    