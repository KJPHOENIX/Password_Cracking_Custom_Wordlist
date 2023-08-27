from itertools import permutations
import time

banner = """
 _  __   _       ____  _   _  ___  _____ _   _ _____  __
| |/ /  | |     |  _ \| | | |/ _ \| ____| \ | |_ _\ \/ /
| ' /_  | |_____| |_) | |_| | | | |  _| |  \| || | \  / 
| . \ |_| |_____|  __/|  _  | |_| | |___| |\  || | /  \ 
|_|\_\___/      |_|   |_| |_|\___/|_____|_| \_|___/_/\_\
                                                        
"""
time.sleep(2)

print(banner)
def gen(): 
     # Get all permutations of string 'ABC'
     time.sleep(2)
     str = input("Enter the Word : ")
     a = int(input("Enter Max length :"))
     permList = permutations(str,a)
 
     # print all permutations
     for perm in list(permList):
         f = open(str+".txt","a")
         f.write(''.join(perm) )
         f.write("\n")
         f.close()
     print("Successfully Generated")
gen()
