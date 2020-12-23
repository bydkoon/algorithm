def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


print(fact(5))


def fact2(n):
    # 문제1의 1부터 n까지 합 구하기
    if n <= 1:
        return 1
    print(n)
    return n + fact2(n - 1)


# [1,2,60,40,130]
def fact3(n):
    # 문제2의 숫자 n개중에서 최대값찾기를 재귀호출로 구하기
    max = n[0]
    for i in range(0, n + 1):
        if max > n:
            return max

    return fact3(n)


# print(fact3([1, 2, 60, 40, 130]))

# print(fact2(5))



def findFact(a):
    result = set()
    n = len(a)
    for i in range(0, n -1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                result.add(a[i])

    return result

if __name__ =="__main__":
    a = ["Apple", "Computer", "Apple", "Bag"]
    print(findFact(a))