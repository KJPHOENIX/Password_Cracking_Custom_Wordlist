from itertools import permutations
 
def gen(): 
     # Get all permutations of string 'ABC'
     str = input("Enter the Word : ")
     a = int(input("Enter Max length :"))
     permList = permutations(str,a)
 
     # print all permutations
     for perm in list(permList):
         f = open(str+".txt","a")
         f.write(''.join(perm) )
         f.write("\n")
         f.close()
gen()