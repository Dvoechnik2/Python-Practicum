import math


def main():
    nums = sorted(set(map(int, input().replace(';', '').split())))
    res = []

    for a in nums:
        mutual_primes = [b for b in nums if a != b and math.gcd(a, b) == 1]
        if mutual_primes:
            res.append(f"{a} - {', '.join(map(str, mutual_primes))}")

    print("\n".join(res))


if __name__ == "__main__":
    main()
