def fibonacci(n: int):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Invalid number")

    if n == 0:
        return []
    if n == 1:
        return [0]

    res = [0, 1]
    for i in range(2, n):
        res.append(res[i - 1] + res[i - 2])
    return res[:n]


def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes(arr):
    if not isinstance(arr, list):
        raise ValueError("Invalid array")

    return [x for x in arr if isinstance(x, int) and is_prime(x)]


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def hcf(arr):
    if not arr:
        raise ValueError("Empty array")

    res = arr[0]
    for num in arr[1:]:
        res = gcd(res, num)
    return res


def lcm(arr):
    if not arr:
        raise ValueError("Empty array")

    res = arr[0]
    for num in arr[1:]:
        res = (res * num) // gcd(res, num)
    return res
