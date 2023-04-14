import math
import random
import sympy

#generating a chosen range of prime numbers
print("Alice, choose a range to generate prime numbers: ")
lowest_limit = int(input("lowest limit: "))
highest_limit= int(input("highest limit: "))

prime_numbers = list(sympy.primerange(lowest_limit,highest_limit +1))
print("Prime numbers within the range u chose: \n", prime_numbers)
print("\n Alice, you can choose numbers from above")

#when entering p, the code provides you information whether that number is prime or not
prime_numberP = int(input("p = "))
if prime_numberP > 1:
    for i in range(2,int(prime_numberP/2)+1):
        if(prime_numberP % i) == 0:
            input("This is not a prime number\n Try again by pressing enter")
            exit()
            break
    else:
        print(prime_numberP, "is a prime number")

else :
    print("This is not a prime number\n Try again by pressing enter")
    exit()

#when entering q, the code provides you information whether that number is prime or not
prime_numberQ = int(input("q = "))
if prime_numberQ > 1:
    for i in range(2,int(prime_numberQ/2)+1):
        if(prime_numberQ % i) == 0:
            input("This is not a prime number\n Try again by pressing enter")
            exit()
            break
    else:
        print(prime_numberQ, "is a prime number")

else :
    print("This is not a prime number\n Try again by pressing enter")
    exit()
n = prime_numberP * prime_numberQ # DO NOT GIVE OUT N!!
phiP = prime_numberP - 1
phiQ = prime_numberQ - 1
phiN = phiP * phiQ #MUST BE KEPT CONFIDENTIAL!

#the purpose of this function is to generate a random number for e such that e and phiN should be coprime(gcd of E and PHIN is 1)
def chooseE(phiN):
    while True:
        e =random.randint(2,phiN-1)
        if math.gcd(e,phiN) == 1:
            return e

e = chooseE(phiN)
print("e = ",e)

# finding all the possible values of modular inverse between 1 and phiN
# and checks if e * i is congruent to 1 modulo phiN and then returns the value of i that sets the seal to the condition
#Since we use E to encrypt, we find the modular inverse of E which is D and is a component of private key along with N
def modular_inverse(e, phiN):
    for i in range(1, phiN):
        if (e * i) % phiN == 1:
            return i
    raise ValueError("THE MODULAR INVERSE DOES NOT EXIST !!")

d = modular_inverse(e, phiN)

Apublic_key =(e, n) # Alice's generated public key
Aprivate_key = (d, n) # Alice's generated private key


#generating a chosen range of prime numbers
print("\nBob, choose a range to generate prime numbers: ")
lowest_limit = int(input("lowest limit: "))
highest_limit= int(input("highest limit: "))

prime_numbers = list(sympy.primerange(lowest_limit,highest_limit +1))
print("Prime numbers within the range u chose: \n", prime_numbers)
print("\n Bob, you can choose numbers from above to enter your prime number")

#when entering p, the code provides you information whether that number is prime or not
Pprime_number = int(input("p = "))
if Pprime_number > 1:
    for i in range(2,int(Pprime_number/2)+1):
        if(Pprime_number % i) == 0:
            input("This is not a prime number\n Try again by pressing enter")
            exit()
            break
    else:
        print(Pprime_number, "is a prime number\n")

else :
    print("This is not a prime number\n Try again by pressing enter")
    exit()

#when entering q, the code provides you information whether that number is prime or not
Qprime_number = int(input("q = "))
if Qprime_number > 1:
    for i in range(2,int(Qprime_number/2)+1):
        if(Qprime_number % i) == 0:
            input("This is not a prime number\n Try again by pressing enter")
            exit()
            break
    else:
        print(Qprime_number, "is a prime number\n")

else :
    print("This is not a prime number\n Try again by pressing enter\n")
    exit()

N = Pprime_number * Qprime_number # DO NOT GIVE OUT N!!
Pphi = Pprime_number - 1
Qphi = Qprime_number - 1
Nphi = Pphi * Qphi #MUST BE KEPT CONFIDENTIAL!

#the purpose of this function is to generate a random number for E such that E and NPHI should be coprime(gcd of E and NPHI is 1)
def choosingE(Nphi):
    while True:
        E =random.randint(2,Nphi-1)
        if math.gcd(E,Nphi) == 1:
            return E

E = choosingE(Nphi)
print("e = ",E)

# finding all the possible values of modular inverse between 1 and phiN
# and checks if e * i is congruent to 1 modulo phiN and then returns the value of i that sets the seal to the condition
#Since we use E to encrypt, we find the modular inverse of E which is D and is a component of private key along with N
def modular_inverse(E, Nphi):
    for i in range(1, Nphi):
        if (E * i) % Nphi == 1:
            return i
    raise ValueError("THE MODULAR INVERSE DOES NOT EXIST !!\n")

D = modular_inverse(E, Nphi)
Bpublic_key = (E, N) #Bob's generated public key
Bprivate_key = (D, N) # Bob's generated private key

message = input("Write the message u want to encrypt:\n")

# encryption using Bobs public key generated above
# It needs Bobs public key to encrypt so Bob can also decrypt using his private key
def encrypt_the_message (Bpublic_key, message):
    E, N = Bpublic_key
    ciphertext = [(ord(char)**E) % N for char in message]
    return ciphertext

theciphertext = encrypt_the_message(Bpublic_key,message)
print(f"Ciphertext:\n {theciphertext}")

#decryption using Bobs private key generated above
def decrypt_the_message(Bprivate_key,theciphertext):
    D, N = Bprivate_key
    plain = [chr((char ** D)%N) for char in theciphertext]
    return ''.join(plain)

theplaintext = decrypt_the_message(Bprivate_key,theciphertext)
print(f'\nPlaintext: {theplaintext}')



