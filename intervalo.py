m = int(input("\nDigite un numero\n\t-->"))
n = int(input("\nDigite otro numero\n\t-->"))

if m < n:
    while m <= n:
        print(m)
        m = m+1
elif m > n:
    while n <= m:
        print(n)
        n = n+1