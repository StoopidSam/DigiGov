from BlockClass import Block


class Blockchain():
    def __init__(self):
        self.chain = [self.createGenesisBlock()]
        self.difficulty = 5

    def createGenesisBlock(self):
        return Block(data={'GENESIS_BLOCK'})

    def getLatestBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]

            if currentBlock.previousHash != previousBlock.hash:
                print('Second test did not pass')
                return False

            else:
                return True
