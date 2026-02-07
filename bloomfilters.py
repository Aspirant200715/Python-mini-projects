#Insert  → O(k)
#Search  → O(k)    number of hash functions

#Why was bloom filters more preffered over linear or hashmap approach 
#Linear has an 0(n) time and space and search complexity 
#HasMap has an 0(1) lookup space but the space constraint doesnt make it a better solution


#The hash functions and the array of bits are both defined by the user 
#Algorithm : As the string is hashcoded and the value of each hashfunction is entered in the bit array 
#Hence if a word is searched again then if all the bits found 1 the says "MAYBE PRESENT" --> "FALSE POSITIVE"
#If any one of the bit is not found then it straight away gives the message of 
# If ANY bit == 0  → Definitely NOT present
# If ALL bits == 1 → Maybe present  (False Positive)

#CODE IMPLEMENTATION

class BloomFilter:
    def _init_(self, size=10):
        self.size = size
        self.bit_array = [0] * size    #Creating bit array
    
    def hash1(self,item):          #hash function 1    
        return sum(ord(x) for x in item) % self.size     #ord function gives the unicode value of the character
    
    def hash2(self, item):
        return (sum(ord(x) for x in item)* 3) % self.size  #hash function 2
    
    def add(self,item):
        self.bit_array[self.hash1(item)] = 1
        self.bit_array[self.hash2(item)] = 1

    def contains(self, item):
        i1 = self.hash1(item)
        i2 = self.hash2(item)
    

    # checking if the bit is present or not 
        if self.bit_array[i1] == 0 or self.bit_array[i2] == 0:
              return False
        return True
    
    #returnin the bit array (without this code the output will be a memeory address)
    def __str__(self):
        return str(self.bit_array)
    

#Test case 
bf = BloomFilter()

bf.add("cat")
bf.add("dog")
bf.add("fish")

print("Bit array:", bf)

print("cat   :", bf.contains("cat"))
print("dog   :", bf.contains("dog"))
print("fish  :", bf.contains("fish"))
print("lion  :", bf.contains("lion"))  # maybe false positive



