import time

def mine_block(last_block, data):

    timestamp = time.time_ns()
    last_hash = last_block.hash
    hash = f'{timestamp}-{last_hash}'

    return Block(timestamp, last_hash, hash, data)

def genesis():
    return Block(1, 'genesis_last_hash', 'genesis_hash', [])

class Block:

    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash 
        self.data = data

    def __repr__(self):
        return (
            f'timestamp : {self.timestamp}, '
            f'last_hash : {self.last_hash}, '
            f'hash : {self.hash}, '
            f'data : {self.data}, '
            )

def main():
    genesis_block = genesis()
    block = mine_block(genesis_block, 'foo')
    print(block)

if __name__ == '__main__':
    main()