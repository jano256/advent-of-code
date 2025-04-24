from functools import cache

def main():
    secret_nums = list(map(int, open("input.txt", "r").read().split()))
    secret_sum = 0
    for secret_num in secret_nums:
        for _ in range(2000):
            secret_num = generate(secret_num)
        secret_sum += secret_num
    print(secret_sum)


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