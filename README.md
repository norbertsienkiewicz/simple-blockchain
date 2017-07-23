# Simple implementation of blockchain.

Each block contains timestamp and index.
Each block has self-identifying hash.

Each block hash is built with index, timestamp, data, hash of previous blok (like in bitcoin).


## Setup
```bash
mkvirtualenv simple-blockchain
workon simple-blockchain
cd src
pip install -r requirements.txt
```

## How to start server?
```bash
python web_server.py
```

## How to create a transaction?
```bash
curl "localhost:5000/transaction" \
     -H "Content-Type: application/json" \
     -d '{"from": "foo", "to":"bar", "amount": 1}'
```

## Hwo to mine a new block?
```bash
curl localhost:5000/mine
```
