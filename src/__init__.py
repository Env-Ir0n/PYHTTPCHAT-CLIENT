import json
import gnupg

print('PyHTTPChat Client SETUP')

username = input('Choose a username: ')

def genkey(email,passphrase):
    GPG = gnupg.GPG
    input_data = GPG.gen_key_input(
        key_type="RSA",
        key_length=2048,
        name_email=email,
        passphrase=passphrase
    )
    key = GPG.gen_key(input_data)
    print(f'key generated for {email} !')
    public_key = GPG.export_keys(key.fingerprint)
    private_key = GPG.export_keys(key.fingerprint, secret=True, passphrase=passphrase)
    print('exporting keys...')

    with open('publickey.asc','w') as f:
        f.write(public_key)

    with open('privatekey.asc','w') as f:
        f.write(private_key)

    print('exported')

haspgp = input('Do you have a PGP key? (Y/n)')
if haspgp == 'Y':
    pass
else:
    print('First we need some info for key generation. This info will not leave your device')
    email = input('Email address: ')
    passphrase = input('Passphrase (REMEMBER THIS): ')
    genkey(email,passphrase)
    
print('saving info...')

with open('client.json') as f:
    jsondata = {'username':username}
    f.write(json.dumps(jsondata))
