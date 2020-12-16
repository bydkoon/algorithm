def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            print("if "+ str(i))
            return i

        i -= 1
        print("while "+ str(i))

if __name__ == "__main__":
    gcd(4,6)
    print(4 % 2)