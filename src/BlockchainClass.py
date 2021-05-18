from BlockClass import Block
from TransactionClass import Transaction


class Blockchain():
    def __init__(self):
        self.difficulty = 2
        self.chain = []
        self.pendingTransactions = []
        self.miningReward = 100

        self.createTransaction(Transaction(None, None, None))
        print('Mining genesis block...')
        self.minePendingTransactions('sam')

    def getLatestBlock(self):
        return self.chain[-1]

    def minePendingTransactions(self, rewardAddress):
        block = Block(self.pendingTransactions)

        try:
            block.previousHash = self.getLatestBlock().hash
        except IndexError:
            block.previousHash = '0' * 64

        block.mineBlock(self.difficulty)

        self.chain.append(block)

        self.pendingTransactions = [Transaction(
            'SYSTEM', rewardAddress, self.miningReward)]

    def createTransaction(self, transaction):
        self.pendingTransactions.append(transaction)

    def getBalance(self, address):
        balance = 0

        for block in self.chain:
            for transaction in block.data:
                if transaction.sender == address:
                    balance -= transaction.amount
                if transaction.receiver == address:
                    balance += transaction.amount

        return balance

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]

            if currentBlock.previousHash != previousBlock.hash:
                return False

            else:
                return True
