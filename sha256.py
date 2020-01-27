import copy
import datetime
import hashlib # Cryptage SHA-256
import random

userID = random.randint(10000, 99999)

class BlockChain():
    def __init__(self): # initialize when creating a chain
        self.blocks = [self.get_genesis_block()]
    
   
    
    def get_genesis_block(self): 
        return Block(0, 
                            datetime.datetime.utcnow(), 
                            'Genesis', 
                            'arbitrary')
    
    def add_block(self, data):
        self.blocks.append(Block(len(self.blocks), 
                                        datetime.datetime.utcnow(), 
                                        data, 
                                        self.blocks[len(self.blocks)-1].hash))
    

    
    
    def fork(self, head='latest'):
        if head in ['latest', 'whole', 'all']:
            return copy.deepcopy(self) # deepcopy since they are mutable
        else:
            c = copy.deepcopy(self)
            c.blocks = c.blocks[0:head+1]
            return c
    


class Block():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashing()
        self.id = userID
    
   
    
    def hashing(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.previous_hash).encode('utf-8'))
        return key.hexdigest()
    



            
c = BlockChain()
for i in range(1,20+1):
    c.add_block(f'This is block {i} of my first chain.')

print(c.blocks[3].timestamp)
print(c.blocks[7].data)
print(c.blocks[9].hash)
print(c.blocks[10].previous_hash)


print(c.blocks[6].id)
print(c.blocks[12].id)
