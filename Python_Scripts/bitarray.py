from bitarray import bitarray
from itertools import product
 
import random
from memory_profiler import profile
 
class BitSequence() :
 
    def __init__(self, choice, size, char_size=2) :
        self._dbit = {}
        self.char_size = char_size
        self.init_bit_gen(char_size)
        self.size = size
        self.choice = choice
        self.gen = self.generator()
        self.init_seq()

    def generator(self):
        for i in range(self.size):
            yield random.choice(self.choice)

    def init_bit_gen(self, char_size) :
        self._bit_gen = product('01', repeat=char_size)
 
    def bit_from_char(self, character) :
        try :
            return self._dbit[character]
 
        except KeyError :
            bit_rep = next(self._bit_gen)
            bit_rep = bitarray(''.join(bit_rep))
            return self._dbit.setdefault(character, bit_rep)
 
    def init_seq(self) :
        self._seq = bitarray(self.size * self.char_size)
        for index, character in enumerate(self.gen):
            index = index * self.char_size
            self._seq[index : index + self.char_size] = self.bit_from_char(character)
 
    def rev_bit_dic(self) :
        return {v.to01() : k for k, v in self._dbit.items()}
 
    def __len__(self) :
        return int(len(self._seq) / self.char_size)
 
    def __setitem__(self, index, value) :
        index = index * self.char_size
        if index >= len(self._seq) :
            raise IndexError()
        self._seq = self._seq[:index] + self.bit_from_char(value) + self._seq[index + self.char_size:]
 
    def __getitem__(self, index) :
        rev_bit_rep = self.rev_bit_dic()
        index = index * self.char_size
        return rev_bit_rep[self._seq[index : index + self.char_size].to01()]
 
    def __str__(self) :
        rev_bit_rep = self.rev_bit_dic()
        return ''.join(rev_bit_rep[self._seq[i:i+self.char_size].to01()] for i in range(0, len(self._seq), self.char_size))
 
 
@profile
def test() :
    choice = "ATGC"
    size = 1000
    #seq = ''.join(random.choice("ATGC") for i in range(1000))
    dna = BitSequence(choice, size)
    #print(dna)
 
test()