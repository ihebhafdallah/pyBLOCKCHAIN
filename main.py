import hashlib
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce = 0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_data.encode('utf-8')).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]
        self.difficulty = 2

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


# Create a new blockchain
my_blockchain = Blockchain()

# Add some data to the blockchain

my_blockchain.add_block(Block(1, date.datetime.now(), {"Temperature C°": 35, "Humidity %": 70}, ""))
my_blockchain.add_block(Block(2, date.datetime.now(), {"Temperature C°": 20, "Humidity %": 50}, ""))
my_blockchain.add_block(Block(3, date.datetime.now(), {"Temperature C°": 18, "Humidity %": 30}, ""))

"""
i = 1
while i < 4:
    temperature = input("Enter Temperature: ")
    humidity = input("Enter Humidity: ")
    my_blockchain.add_block(Block(i, date.datetime.now(), {"Temperature": temperature, "Humidity": humidity}, ""))
    i += 1
"""

# Print the blockchain
for block in my_blockchain.chain:
    print("Index:", block.index)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Nonce:", block.nonce)
    print("Previous Hash:", block.previous_hash)
    print("")

# Check if the blockchain is valid
print("Is the blockchain valid? " + str(my_blockchain.is_chain_valid()))
