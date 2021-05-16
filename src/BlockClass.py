import time
from hashlib import sha256


class Block():
    def __init__(self, data=None):
        self.timestamp = str(time.time())
        self.data = data
        self.previousHash = '0'*64
        self.hash = self.calculateHash()
        self.nonce = 0

        self.dict = {
            "Previous hash": self.previousHash,
            "Hash": self.hash,
            "Timestamp": self.timestamp,
            "Data": self.data
        }

    def mineBlock(self, difficulty):
        while self.hash[:difficulty] != '0'*difficulty:
            self.nonce += 1
            self.calculateHash()

        print('Block mined: ' + self.hash)

    def calculateHash(self):
        hashingText = f'{self.timestamp}{self.data}{self.previousHash}{self.nonce}'.encode(
            'utf-8')

        return sha256(hashingText).hexdigest()
