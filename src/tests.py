from BlockchainClass import Blockchain
from BlockClass import Block
import json

blockchain = Blockchain()
blockchain.addBlock(Block(data='Sam votes for Jeff'))
blockchain.addBlock(Block(data='Jake votes for Jeff'))
blockchain.addBlock(Block(data='Eliza votes for Bob'))
blockchain.addBlock(Block(data='Hannah votes for Bob'))

print(blockchain.chain)
print(blockchain.isChainValid())
