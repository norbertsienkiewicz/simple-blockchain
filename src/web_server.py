import datetime as dt
import json
import requests

from flask import Flask, request

from block import Block
from genesis import create_genesis_block
from proof_of_work import proof_of_work


node = Flask(__name__)


# Random address of the owner of this node
miner_address = "a-random-miner-address-t2g329873ty51"

blockchain = []
blockchain.append(create_genesis_block())
this_nodes_transactions = []
# list of other nodes in system aka other blockchain users
peer_nodes = []


def log_new_transaction(transaction):
    print "New transaction"
    print "FROM: {}".format(transaction['from'])
    print "TO: {}".format(transaction['to'])
    print "AMOUNT: {}".format(transaction['amount'])

@node.route('/transaction', methods=['POST'])
def transaction():
    if request.method == 'POST':
        new_transaction = request.get_json()
        this_nodes_transactions.append(new_transaction)
        log_new_transaction(new_transaction)
        return "Transaction submission successfull\n"

@node.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain[len(blockchain) - 1]
    last_proof = last_block.data['proof-of-work']
    # mine
    proof = proof_of_work(last_proof)
    this_nodes_transactions.append(
        { "from": "network", "to": miner_address, "amount": 1 }
    )
    # gather data
    new_block_data = {
        "proof-of-work": proof,
        "transactions": list(this_nodes_transactions),
    }
    new_block_index = last_block.index + 1
    new_block_timestamp = dt.datetime.now()
    last_block_hash = last_block.hash
    this_nodes_transactions[:] = []
    # create new block
    mined_block = Block(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash,
    )
    blockchain.append(mined_block)
    return json.dumps({
        "index": new_block_index,
        "timestamp": str(new_block_timestamp),
        "data": new_block_data,
        "hash": last_block_hash,
    }) + "\n"

@node.route('/blocks', methods=['GET'])
def get_blocks():
    chain_to_send = blockchain
    for block in chain_to_send:
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = block.hash
        block = {
            "index": block_index,
            "timestamp": block_timestamp,
            "data": block_data,
            "hash": block_hash
        }
    chain_to_send = json.dumps(chain_to_send)
    return chain_to_send


def find_new_chains():
    other_chains = []
    for node_url in peer_nodes:
        block = requests.get(node_url + "/blocks").content
        block = json.loads(block)
        other_chains.append(block)
    return other_chains

# Make sure we have same chain on every node
# MORE: https://en.wikipedia.org/wiki/Consensus_%28computer_science%29
def consensus():
    other_chains = find_new_chains()
    longest_chain = blockchain
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain
    blockchain = longest_chain

node.run()
