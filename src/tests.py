from BlockchainClass import Blockchain
from BlockClass import Block
from TransactionClass import Transaction


print('\nStarting miner...')
blockchain = Blockchain()
print('\nCreating some new transactions...')
blockchain.createTransaction(Transaction('sam', 'eliza', 10))
blockchain.createTransaction(Transaction('sam', 'bill', 10))
print('\nMining the new transactions...')
blockchain.minePendingTransactions('sam')
print(f'Sam\'s balance: ' + str(blockchain.getBalance('sam')))
