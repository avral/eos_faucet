# eos_faucet
Service for create accounts in eos blockchain.

## Build Docker image
`docker build -t eos_faucet .`

## Run Docker image
1. Create .env file
2. upgrade database `docker-compose --rm upgrade`
3. create user for admin page `docker-compose --rm base python manage.py createsuperuser`
3. app lisen you requests on `http://127.0.0.1:8000`
4. admin page: `http://127.0.0.1:8000/admin/`


## Api methods

### Get sms code
POST request to /api/pass-code/
`number: phone number`


### Create account
POST request to /api/account/

```
account: eos_new_account_name
owner_pub: eos_owner_pub_key
active_pub: eos_active_pub_key
number: phone number
passcode: sms code
```

## .env file example
```
EOS_NODE_URL=https://..
EOS_NODE_PORT=443

REGISTRATOR_NAME=faucet
REGISTRATOR_WIF=5JXi2..

TWILLIO_SID=..
TWILLIO_TOKEN=..
```

## request example
````
http :8000/account name=adf owner_pub=<owner pub key> active_pub=<active pub key>
