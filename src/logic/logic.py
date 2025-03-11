class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    """
    
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def secuencia_fibonacci(self, n):
        seq = [0, 1]
        for _ in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq[:n]
    
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        return [i for i in range(2, n+1) if self.es_primo(i)]
    
    def es_numero_perfecto(self, n):
        if n <= 0:
            return False
        return n == sum(i for i in range(1, n) if n % i == 0)
    
    def triangulo_pascal(self, filas):
        triangulo = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(triangulo[i-1][j-1] + triangulo[i-1][j])
            fila.append(1)
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        return 1 if n == 0 else n * self.factorial(n - 1)
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        return sum(int(d) for d in str(n))
    
    def es_numero_armstrong(self, n):
        num_str = str(n)
        return n == sum(int(d)**len(num_str) for d in num_str)
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        suma_objetivo = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_objetivo:
                return False
        
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        
        if sum(matriz[i][n-i-1] for i in range(n)) != suma_objetivo:
            return False
        
        return True

class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        return a and b
    
    def OR(self, a, b):
        return a or b
    
    def NOT(self, a):
        return not a
    
    def XOR(self, a, b):
        return a != b
    
    def NAND(self, a, b):
        return not (a and b)
    
    def NOR(self, a, b):
        return not (a or b)
    
    def XNOR(self, a, b):
        return a == b
    
    def implicacion(self, a, b):
        return not a or b
    
    def bi_implicacion(self, a, b):
        return a == b
