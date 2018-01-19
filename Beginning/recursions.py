def count_vowels(s, i = 0):

    if (i == len(s)): return 0

    c = s[i]
    if c in 'aeiou':
        return count_vowels(s, i + 1) + 1
    return count_vowels(s, i + 1) + 0


# print(count_vowels('hello'))
# print(count_vowels('world'))


def digit_sum(n):
    if n == 0: return 0
    return digit_sum(n//10) + n % 10


# print(digit_sum(345))
# print(digit_sum(456))


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-2) + fib(n-1)


# for i in range(10):
#     print(fib(i))