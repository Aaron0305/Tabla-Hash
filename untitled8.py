class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize the table with None

    def _calculate_operation(self, value):
        digits = [int(digit) for digit in str(value) if digit.isdigit()][:3]
        result = (digits[0] + digits[1]) * digits[2] if len(digits) == 3 else value
        return result

    def _calculate_hash(self, key):
        return key % self.size

    def insert(self, key):
        calculated_value = self._calculate_operation(key)
        hash_value = key % self.size  # Fix: Use key directly for calculating hash value
        self.place_value(hash_value, key, calculated_value)

    def search(self, value):
        for entry in self.table:
            if entry and self._calculate_operation(entry[0]) == value:
                return entry[0]

        return None

    def delete(self, key):
        hash_value = key % self.size  # Fix: Use key directly for calculating hash value
        self.table[hash_value] = None

    def search_by_index(self, index):
        entry = self.table[index]
        if entry:
            print(f"Clave en el índice {index}: {entry[0]}")
        else:
            print(f"No hay clave en el índice {index}")

    def place_value(self, hash_value, key, calculated_value):
        if self.table[hash_value] is None:
            self.table[hash_value] = (key, calculated_value)
        else:
            # Manejar colisiones (por ejemplo, usando encadenamiento)
            # Aquí puedes implementar tu lógica específica para manejar colisiones
            pass

def print_menu():
    print("1. Insertar elemento")
    print("2. Buscar clave por resultado de operación")
    print("3. Eliminar elemento por clave")
    print("4. Mostrar clave en un índice")
    print("5. Salir")

# Example usage of the menu
size = int(input("Ingrese la cantidad de datos que desea contener en el arreglo: "))
hash_table = HashTable(size)

while True:
    print("\nTabla Hash:", hash_table.table)
    print_menu()
    choice = input("Selecciona una opción (1-5): ")

    if choice == "1":
        key = int(input("Ingrese la clave (formato: 123): "))
        hash_table.insert(key)
    elif choice == "2":
        value = int(input("Ingrese el resultado de la operación a buscar: "))
        result_key = hash_table.search(value)
        if result_key is not None:
            print(f"Clave encontrada: {result_key}")
        else:
            print(f"No se encontró ninguna clave asociada al resultado {value}")
    elif choice == "3":
        key = int(input("Ingrese la clave a eliminar: "))
        hash_table.delete(key)
        print(f"Clave '{key}' eliminada.")
    elif choice == "4":
        index = int(input("Ingrese el índice a mostrar: "))
        hash_table.search_by_index(index)
    elif choice == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija nuevamente.")
