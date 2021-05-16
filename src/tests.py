from BlockchainClass import Blockchain
from BlockClass import Block
import json

blockchain = Blockchain()
blockchain.addBlock(Block(data='Sam votes for Jeff'))
blockchain.addBlock(Block(data='Eliza votes for Bob'))
blockchain.addBlock(Block(data='Jake votes for Bob'))
blockchain.addBlock(Block(data='Hanna votes for Jeff'))

if blockchain.isChainValid:
    print('\nBlockchain is valid!')
else:
    print('Blockchain is not valid.')
