
# import math

# N = int(input())
# start_num = 10**(N-1)
# end_num = 10**N
# primenum = [2, 3, 5, 7]

# # If N is 1
# if N == 1:
#     start_num = 1
#     end_num = 10
#     for j in primenum:
#         print(j)

# def is_prime(num):
#     if num < 2:
#         return False
#     for j in range(2, int(math.sqrt(num)) + 1):
#         if num % j == 0:
#             return False
#     return True

# def search(num):
#     ans = ""
#     for i in str(num):
#         ans += i
#         Pr = int(ans)
#         if not is_prime(Pr):
#             return
#     print(num)

# for i in range(start_num, end_num):
#     if i % 10 in [1, 3, 7, 9]:  # Only check numbers ending in 1, 3, 7, 9 (odd digits except 5)
#         search(i)
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(int(num**0.5)) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(current, N):
    if len(str(current)) == N:
        print(current)
        return
    for digit in range(1, 10):  # Digits 1 through 9
        new_number = current * 10 + digit
        if is_prime(new_number):
            generate_primes(new_number, N)

N = int(input())
if N == 1:
    primenum = [2, 3, 5, 7]
    for prime in primenum:
        print(prime)
else:
    for prime in [2, 3, 5, 7]:  # Start with single-digit primes
        generate_primes(prime, N)
