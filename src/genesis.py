# genesis block is special initial block with index 0

import datetime as dt

from block import Block


def create_genesis_block():
    return Block(0, dt.datetime.now(), {
        "proof-of-work": 9,
        "transactions": None
    }, "0")
