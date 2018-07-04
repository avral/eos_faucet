# eos_faucet
Service for create accounts in eos blockchain.

## Build Docker image
`docker build -t eos_faucet .`

## Run Docker image
1. Create .env file
2. run docker `docker run --rm -it --env-file .env -p 8000:5000 eos_faucet`

## .env file example
```
EOS_NODE_URL=https://..
EOS_NODE_PORT=443

REGISTRATOR_NAME=faucet
REGISTRATOR_WIF=5JXi2..
```
