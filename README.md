# simple-blockchain

Simple implementation of blockchain.

Each block contains timestamp and index.
Each block has self-identifying hash.

Each block hash is built with index, timestamp, data, hash of previous blok (like in bitcoin).


Transation example:
```json
{
  "from": "71238uqirbfh894-random-public-key-a-alkjdflakjfewn204ij",
  "to": "93j4ivnqiopvh43-random-public-key-b-qjrgvnoeirbnferinfo",
  "amount": 3
}
```


## Setup
```bash
mkvirtualenv simple-blockchain
workon simple-blockchain
cd src
pip install -R requirements.txt
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
