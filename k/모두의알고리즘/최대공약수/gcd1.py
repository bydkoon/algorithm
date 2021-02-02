def gcd(a, b):
    i = min(a, b)
    print(i)
    while True:
        if a % i == 0 and b % i == 0:
            print("if "+ str(i))
            return i

        i -= 1
        print("while "+ str(i))

if __name__ == "__main__":
    x = 4
    t = 6
    print('gcd')
    gcd(x,t)

    print('gcd2')
    gcd(t,x % t)
    print('-0-------')
    print(6 % 4)