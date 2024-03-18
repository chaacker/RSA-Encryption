import random as r
import math

def main():
    p = gen_prime(1, 1000)
    q = gen_prime(1, 1000)
    while p == q:
        q = gen_prime(1, 1000)

    n  = p * q
    lambda_n = private_key(p, q)

    e = r.randint(3, lambda_n - 1)
    while math.gcd(e, lambda_n) != 1:
        e = r.randint(3, lambda_n - 1)

    d = mod_multi_inverse(e, lambda_n)

    message = input("Write your message here: ")

    encode_message = []
    cipher = []
    with open("encoded_text.txt", "w") as file:
        file.write(f"{message}\n")
        for char in message:
            encode_message.append(ord(char))
        file.write(f"{str(encode_message)}\n")
        for c in encode_message:
            cipher.append(pow(c, e, n))
        file.write(f"{str(cipher)}\n")

    decoded_message = []
    original_message_list = []
    with open("decoded_text.txt", "w") as file:
        for char in cipher:
            decoded_message.append(pow(char, d, n))
        file.write(f"{str(decoded_message)}\n")
        for char in decoded_message:
            letter = "".join(chr(char))
            original_message_list.append(letter)
        file.write(f"{str(original_message_list)}\n")
        original_message = "".join(original_message_list)
        file.write(f"{original_message}\n")

def gen_prime(min, max):
    prime = r.randint(min, max)
    while not is_prime(prime):
        prime = r.randint(min, max)
    return prime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def private_key(p, q):
    lambda_n = math.lcm(p - 1, q - 1)
    return lambda_n

def mod_multi_inverse(e, lambda_n):
    for d in range(3, lambda_n):
        if (d * e) % lambda_n == 1:
            return d
        else:
            continue

if __name__ == "__main__":
    main()
