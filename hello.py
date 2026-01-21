def main():
    print("Hello World")

def print_factor(x):
    print(f"{x}'s factors is ",end='')
    for i in range(2, x):
        # your code here
        if x % i == 0:
            print(i, end=' ')
    print()

if __name__ == '__main__':
    main()

    x = 52633
    print_factor(x)

    l = [52633, 8137, 1024, 999]
    for i in l:
        print_factor(i)