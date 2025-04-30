from functools import cache

def main():
    secret_nums = list(map(int, open("test.txt", "r").read().split()))
    sequences = []
    for secret_num in secret_nums:
        sequences.append([])
        for _ in range(1999):
            new_secret_num = generate(secret_num)
            sequences[-1].append((new_secret_num % 10, new_secret_num % 10 - secret_num % 10))
            secret_num = new_secret_num
    #print(sequences)


def generate(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret

def mix(secret, value):
    return value ^ secret

def prune(secret):
    return secret % 16777216

main()