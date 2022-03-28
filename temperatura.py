grados_f = float(input("digita la temperatura en grados Farenheit\n\t-->"))

grados_c = float((grados_f - 32) / (1.8))
grados_k = float((((5) * (grados_f - 32)) / 9) + 273.15)

print(f"""Temperatura en Fahrenheit: {grados_f:.2f}
Temperatura en Celsius: {grados_c:.2f}
Temperatura en Kelvin: {grados_k:.2f}""")