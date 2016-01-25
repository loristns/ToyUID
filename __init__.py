import platform
import random
import time
from uuid import getnode
import timeit
import hashlib

class ToyUID:

    def __init__(self, domain=getnode()):

        timestamp1 = time.time()

        randomnumber1 = random.randrange(1000000000000000000)
        randomnumber2 = random.randrange(randomnumber1) #randomnumber2 is equal of inferior to randomnumber1
        randomnumber3 = random.randrange(randomnumber1 * randomnumber2)
        randomnumber4 = random.uniform(1, 100) / 50 #only used to get timestamp2

        #getting an random list of word
        wordfile = open('ToyUID/french.txt', 'r')
        word = wordfile.readlines()
        wordlist = []
        for element in word:
            wordlist.append(element.replace('\n', ''))

        random.shuffle(wordlist)
        wordlen = len(wordlist)

        self.word = wordlist[random.randrange(wordlen)] #get a totally random word

        #get some computer's data like os name, processor architecture and mac adress
        self.arch = platform.machine()
        self.os = platform.platform()
        self.mac = str(domain).encode('utf-8')
        self.mac = hashlib.sha224(self.mac).hexdigest() #hash mac address for better privacy


        #get computer performance estimation with loading of a big python standard module : tkinter
        performance = timeit.Timer("while i != 11: i = random.randrange(1000000)", 'i = 0; import random')
        self.timeget = performance.timeit()

        #get timestamp2 at the end
        time.sleep(randomnumber4)
        self.timestamp2 = time.time()

        #now create ToyUID

        self.UIDlist = [str(timestamp1),
                        str(randomnumber1),
                        str(randomnumber2),
                        str(randomnumber3),
                        self.word,
                        self.arch,
                        self.os,
                        self.mac,
                        str(self.timeget),
                        str(self.timestamp2),
                        ]

        random.shuffle(self.UIDlist) #randomly change the list's order

        #hash the ToyUID with an random algorithm

        self.hash_algorithm = random.choice(list(hashlib.algorithms_available))
        hashing = hashlib.new(self.hash_algorithm)

        for element in self.UIDlist:
            element = element + random.choice("azertyuiopqsdfghjklmwxcvbn1234567890") #add a random salt
            element = element.encode('utf-8')
            hashing.update(element)

        self.UIDhash = hashing.hexdigest()[:35] #get 35 first caracter of the hash

    def __bytes__(self):
        """send a bytes ToyUID"""
        return bytes(self.UIDhash, 'utf-8')

    def __str__(self):
        """send a str ToyUID"""
        return self.UIDhash

    def __int__(self):
        """send a int ToyUID"""
        return int(self.UIDhash, 16)

    @property
    def generate_list(self):
        """send the parameter's list used for generating ToyUID"""
        return self.UIDlist

    @property
    def algorithm(self):
        """send the algorithm name selected"""
        return self.hash_algorithm
