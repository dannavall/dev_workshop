class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    """
    
    def es_palindromo(self, texto):
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
        return texto_limpio == texto_limpio[::-1]

    def invertir_cadena(self, texto):
        resultado = ""
        for char in texto:
            resultado = char + resultado
        return resultado

    def contar_vocales(self, texto):
        return sum(1 for c in texto.lower() if c in "aeiouáéíóú")

    def contar_consonantes(self, texto):
        return sum(1 for c in texto.lower() if c.isalpha() and c not in "aeiouáéíóú")

    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())

    def contar_palabras(self, texto):
        return len(texto.split())

    def palabras_mayus(self, texto):
        return ' '.join(p.capitalize() for p in texto.split())

    def eliminar_espacios_duplicados(self, texto):
        return ' '.join(texto.split())

    def es_numero_entero(self, texto):
        if texto.strip() and (texto[0] == '-' or texto[0].isdigit()):
            return texto[1:].isdigit() if texto[0] == '-' else texto.isdigit()
        return False

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                resultado += chr((ord(char) - offset + desplazamiento) % 26 + offset)
            else:
                resultado += char
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i+len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones
