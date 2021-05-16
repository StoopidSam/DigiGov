from BlockClass import Block


class Blockchain():
    def __init__(self):
        self.difficulty = 5
        self.chain = []

        genesisBlock = Block(data={'GENESIS_BLOCK'})
        self.addBlock(genesisBlock)

    def createGenesisBlock(self):
        genesisBlock = Block(data={'GENESIS_BLOCK'})
        self.addBlock(genesisBlock)

    def getLatestBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        try:
            newBlock.previousHash = self.getLatestBlock().hash
        except IndexError:
            newBlock.previousHash = '0' * 64

        newBlock.mineBlock(self.difficulty)
        self.chain.append(newBlock)

    def isChainValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i-1]

            if currentBlock.previousHash != previousBlock.hash:
                return False

            else:
                return True
