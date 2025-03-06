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
        return (not a) or b
    
    def bi_implicacion(self, a, b):
        return a == b
    
# Ejemplo de uso
if __name__ == "__main__":
    logica = Logica()
    operaciones = {
        "AND": (True, False),
        "OR": (True, False),
        "NOT": (True,),
        "XOR": (True, False),
        "NAND": (True, True),
        "NOR": (False, False),
        "XNOR": (True, True),
        "Implicación": (True, False),
        "Bi-Implicación": (True, True)
    }
    
    for nombre, args in operaciones.items():
        metodo = getattr(logica, nombre)
        resultado = metodo(*args)
        print(f"{nombre}({', '.join(map(str, args))}): {resultado}")