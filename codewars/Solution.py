import numpy as np
import math

knight_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]



def knight(p1, p2):
    map = np.zeros((8, 8))
    xy = algebraic_to_eucledian(p1)
    xyt = algebraic_to_eucledian(p2)

    map[xy] = 1

    iter = 1
    while True:
        for x, y in [range(s) for s in range(8)]:
            # for y in range(8):
            if (x, y) == xyt and map[x, y] > 0:
                return map[x, y] - 1

            if map[x, y] == iter:
                for jx, jy in knight_moves:
                    if 8 > x + jx >= 0 and 0 <= y + jy < 8 and map[x + jx, y + jy] == 0:
                        map[x + jx, y + jy] = iter + 1
        iter = iter + 1


def algebraic_to_eucledian(p):
    return ('abcdefgh'.index(p[0]), int(p[1]) -1)

    # start here!


def listPosition(word):
    """Return the anagram list position of the word"""
    if len(word) == 0:
        return 0
    if len(word) == 1:
        return 1
    ans = 0
    for s in sorted(set(word)):
        if word[0] == s:
            ans = ans + listPosition(word[1:])
            return ans
        else:
            ans += combination(word.replace(s, '', 1))

    return ans


def combination(word):
    d = 1
    for w in set(word):
        d = d * math.factorial(word.count(w))
    return math.factorial(len(word)) // d


def fibonacci(n, cache={}):
    if n in [0, 1]:
        return n
    if n in cache:
        return cache[n]
    ans = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    cache[n] = ans
    return ans


def snail(snail_map):
    if len(snail_map) == 0:
        return []

    if len(snail_map) == 1 and len(snail_map[0]) == 0:
        return []

    if len(snail_map) == 1:
        return [snail_map[0][0]]

    n = len(snail_map)

    ans = []

    y, x = 0, 0
    for x in range(0, n):
        ans += [snail_map[y][x]]
    for y in range(1, n):
        ans += [snail_map[y][x]]
    for x in range(n - 2, -1, -1):
        ans += [snail_map[y][x]]
    for y in range(n - 2, 0, -1):
        ans += [snail_map[y][x]]

    a = np.array(snail_map)

    return ans + snail(a[1:n - 1, 1:n - 1])


def scramble(s1, s2):
    m1, m2 = {}, {}
    for s in s1:
        m1[s] = m1.get(s, 0) + 1
    for s in s2:
        m2[s] = m2.get(s, 0) + 1

    for symbol, numOfSymbols in m2.items():
        if m1.get(symbol) is None or m1[symbol] < numOfSymbols:
            return False
    return True


def scramble2(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    len_s1 = len(s1)
    index1 = -1
    for char2 in s2:
        while True:
            index1 += 1
            if index1 >= len_s1:
                return False
            if char2 == s1[index1]:
                break
    return True


def maxSequence(arr):
    if len(arr) == 0:
        return 0
    ans = 0
    sum = 0
    for n in arr:
        sum += n
        if sum > ans:
            ans = sum
        if sum <= 0:
            sum = 0
    return ans


keyMap = {'(': ')', '[': ']', '{': '}'}


def validBraces(string):
    if len(string) == 0:
        return True
    ans, ignore = validBraces2(string, '', 0)
    return ans


def validBraces2(string, open, index):
    while index < len(string):
        s = string[index]
        index += 1
        if s in keyMap.keys():
            right, index = validBraces2(string, s, index)
            if not right:
                return False, index
        elif open == '':
            return False, index
        elif s == keyMap[open]:
            return True, index
        else:
            return False, index

    return (True, index) if open == '' else (False, index)
