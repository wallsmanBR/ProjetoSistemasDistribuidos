import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

        #Cria o bloco genesis
        self.new_block(previous_hash=1, proof=100)

    # Cria um bloco em uma blockchain
    # Proof é um int e é a prova dada pelo algoritmo de Proof of Work
    # Previous_hasg é uma string opcional do hash do bloco anterior
    # Retorna um novo bloco
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        #Reset a lista atual de transações
        self.current_transaction = []
        self.chain.append(block)
        return block


    # Add transação a um bloco
    # Esse metodo retorna um int que eh o index do bloco que tera essa transação
    # Os parametro sender e recipient são string e o amount eh um int
    def new_transaction(self, sender, recipient, amount):
        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index']+1

    @property
    def last_block(self):
        return self.chain[-1]

    # Cria um hash para o block (SHA-256)
    # Retorna uma string
    @staticmethod
    def hash(block):
        # Ordena o dicionario, para ter certeza que nao havera inconsistencia nos hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

