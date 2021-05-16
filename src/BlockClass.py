import time
from hashlib import sha256


class Block():
    def __init__(self, data=None):
        self.timestamp = str(time.time())
        self.data = data
        self.previousHash = '0'*64
        self.nonce = 0
        self.hash = self.calculateHash()

    def getBlockDict(self):
        return {
            "Previous hash": self.previousHash,
            "Hash": self.hash,
            "Timestamp": self.timestamp,
            "Data": self.data,
            "Nonce": self.nonce
        }

    def mineBlock(self, difficulty):
        while True:
            if self.hash[:difficulty] != '0' * difficulty:
                self.nonce += 1
                self.hash = self.calculateHash()
            else:
                print(f'Block mined: {self.hash}')
                break

    def calculateHash(self):
        hashingText = f'{self.timestamp}{self.data}{self.previousHash}{self.nonce}'.encode(
            'utf-8')

        return sha256(hashingText).hexdigest()
