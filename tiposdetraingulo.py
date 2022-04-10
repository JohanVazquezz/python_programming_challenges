a = input("\ndigita el valor de a\n\t-->")
b = input("\ndigita el valor de b\n\t-->")
c = input("\ndigita el valor de c\n\t-->")

if a == b and a == c:
    print("\nRE: Triangulo equilatero")
elif a == b or a == c or b == c:
    print("\nRE: Triangulo isoceles")
else:
    print("\nRE: Triangulo Escaleno")