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

        word = wordlist[random.randrange(wordlen)] #get a totally random word

        #get some computer's data like os name, processor architecture and mac adress
        arch = platform.machine()
        os = platform.platform()
        mac = str(domain).encode('utf-8')
        mac = hashlib.sha1(mac).hexdigest() #hash mac address for better privacy


        #get computer performance estimation with loading of a big python standard module : tkinter
        performance = timeit.Timer("while i != 11: i = random.randrange(1000000)", 'i = 0; import random')
        timeget = performance.timeit()

        #get timestamp2 at the end
        time.sleep(randomnumber4)
        timestamp2 = time.time()

        #now create ToyUID

        UIDlist = [str(timestamp1),
                        str(randomnumber1),
                        str(randomnumber2),
                        str(randomnumber3),
                        word,
                        arch,
                        os,
                        mac,
                        str(timeget),
                        str(timestamp2),
                        ]

        random.shuffle(UIDlist) #randomly change the list's order

        #hash the ToyUID with an random algorithm

        self.algorithm = random.choice(list(hashlib.algorithms_available))
        hashing = hashlib.new(self.algorithm)

        for element in UIDlist:
            element = element + random.choice("azertyuiopqsdfghjklmwxcvbn1234567890") #add a random salt
            element = element.encode('utf-8')
            hashing.update(element)

        self.str = hashing.hexdigest()[:35] #get 35 first caracter of the hash
        self.bytes = bytes(self.str, 'utf-8') #get bytes
        self.int = int(self.str, 16)

    def __bytes__(self):
        """send a bytes ToyUID"""
        return self.bytes

    def __str__(self):
        """send a str ToyUID"""
        return self.str

    def __int__(self):
        """send a int ToyUID"""
        return self.int