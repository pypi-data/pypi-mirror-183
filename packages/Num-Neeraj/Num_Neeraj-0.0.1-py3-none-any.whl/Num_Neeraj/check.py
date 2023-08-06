
def is_Prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print('False')
                break
            else:
                print("True")
    else:
        print("False")

def is_even(num):
    if int(num) <= 0:
        print('False')
    if int(num) % 2 == 0:
        print('True')
    else:
        print('False')

def is_odd(num):
    if int(num) <= 0:
        print('False')
    if int(num) % 2 != 0:
        print(True)
    else:
        print('False')

def is_negative(num):
    if int(num) < 0:
        print('True')
    else:
        print('False')
        
def is_Palindrome(num):
    s = str(num)
    p = s[::-1]
    if p == s:
        print("True")
    else:
        print("False")

def getTwinPrime(n):
    prime = [True for i in range(n + 2)]
    p = 2
    
    while (p * p <= n + 1):
        if (prime[p] == True):
            for i in range(p * 2, n + 2, p):
                prime[i] = False
                p += 1

    for p in range(2, n-1):
        if prime[p] and prime[p + 2]:
            print("(",p,",", (p + 2), ")" ,end='')
