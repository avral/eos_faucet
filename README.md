# eos_faucet
Service for create accounts in eos blockchain.

## Build Docker image
`docker build -t eos_faucet .`

## Run Docker image
1. Create .env file
2. run docker `docker run --rm -it --env-file .env -p 8000:5000 eos_faucet`
3. app lisen you requests on `http://127.0.0.1:8000`
4. create POST request to 127.0.0.1:8000/account

request format:
method: POST

```
name: eos_new_account_name
owner_pub: eos_owner_pub_key
active_pub: eos_active_pub_key
```

## .env file example
```
EOS_NODE_URL=https://..
EOS_NODE_PORT=443

REGISTRATOR_NAME=faucet
REGISTRATOR_WIF=5JXi2..
```

## request example
````
http :8000/account name=adf owner_pub=<owner pub key> active_pub=<active pub key>
