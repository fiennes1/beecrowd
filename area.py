a, b, c = [float(x) for x in input().split()]

pi = 3.14159
triangle = (a * c) / 2
circle = pi * c ** 2
trapezium = ((a + b) * c) / 2
square = b ** 2
rectangle = a * b

print(f'TRIANGULO: {triangle:.3f}\n'
      f'CIRCULO: {circle:.3f}\n'
      f'TRAPEZIO: {trapezium:.3f}\n'
      f'QUADRADO: {square:.3f}\n'
      f'RETANGULO: {rectangle:.3f}')
