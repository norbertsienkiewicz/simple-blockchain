# A proof of work is a piece of data which is difficult
# (costly, time-consuming) to produce but easy for others to verify and
# which satisfies certain requirements.
# MORE: https://en.bitcoin.it/wiki/Proof_of_work


# simple pow
def proof_of_work(last_proof):
    incrementor = last_proof + 1
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    return incrementor

