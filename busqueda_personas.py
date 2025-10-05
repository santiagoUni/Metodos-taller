import random
from datetime import datetime, timedelta

def busqueda_recursiva_personas(personas, criterio, inicio=0, fin=None):
    if fin is None:
        fin = len(personas)
    if inicio >= fin:
        return []
    if fin - inicio == 1:
        if criterio(personas[inicio]):
            return [personas[inicio]]
        return []
    mid = (inicio + fin) // 2
    izq = busqueda_recursiva_personas(personas, criterio, inicio, mid)
    der = busqueda_recursiva_personas(personas, criterio, mid, fin)
    return izq + der

def buscar_por_nombre_inicial(personas, letra):
    return busqueda_recursiva_personas(personas, lambda p: p['nombre'].startswith(letra))

def buscar_por_fecha_nacimiento(personas, fecha_limite):
    return busqueda_recursiva_personas(personas, lambda p: str(p['fecha_nacimiento']) < fecha_limite)

def generar_personas():
    nombres = [
        'Ana García', 'Carlos López', 'María Rodríguez', 'Juan Martínez', 'Laura Sánchez',
        'Pedro Fernández', 'Isabel González', 'Antonio Pérez', 'Carmen Ramírez', 'Miguel Torres',
        'Rosa Díaz', 'Francisco Muñoz', 'Elena Cruz', 'José Hernández', 'Marta Jiménez',
        'David Moreno', 'Lucía Ruiz', 'Manuel Álvarez', 'Patricia Romero', 'Alejandro Navarro',
        'Sara Gutiérrez', 'Roberto Molina', 'Andrea Castro', 'Javier Ortiz', 'Cristina Delgado',
        'Alberto Ramírez', 'Beatriz Vega', 'Fernando Silva', 'Silvia Mendoza', 'Ricardo Vargas',
        'Julia Morales', 'Ángel Rojas', 'Raquel Medina', 'Sergio Aguilar', 'Natalia Iglesias',
        'Pablo Giménez', 'Victoria Cabrera', 'Adrián Núñez', 'Irene Fuentes', 'Rubén Márquez',
        'Carolina Serrano', 'Daniel Campos', 'Verónica Carrasco', 'Marcos Vidal', 'Teresa León',
        'Ignacio Cano', 'Pilar Cortés', 'Guillermo Prieto', 'Alicia Méndez', 'Emilio Pascual',
        'Ana Martín', 'Carlos Sanz', 'María Domínguez', 'Juan Rubio', 'Laura Calvo',
        'Pedro Bravo', 'Isabel Soler', 'Antonio Gil', 'Carmen Merino', 'Miguel Benítez',
        'Rosa Blanco', 'Francisco Suárez', 'Elena Mora', 'José Espinosa', 'Marta Herrera',
        'David Montero', 'Lucía Lozano', 'Manuel Parra', 'Patricia Gallego', 'Alejandro Esteban',
        'Sara Guerrero', 'Roberto Velasco', 'Andrea Lorenzo', 'Javier Ibáñez', 'Cristina Moya',
        'Alberto Caballero', 'Beatriz Flores', 'Fernando Peña', 'Silvia Santana', 'Ricardo Carmona',
        'Julia Marín', 'Ángel Soto', 'Raquel Reyes', 'Sergio Vázquez', 'Natalia León',
        'Pablo Herrero', 'Victoria Ortega', 'Adrián Crespo', 'Irene Román', 'Rubén Santos',
        'Carolina Méndez', 'Daniel Nieto', 'Verónica Pastor', 'Marcos Hidalgo', 'Teresa Benito',
        'Ignacio Durán', 'Pilar Ferrer', 'Guillermo Vicente', 'Alicia Arias', 'Emilio Carrillo'
    ]
    personas = []
    inicio = datetime(1945, 1, 1)
    fin = datetime(2005, 12, 31)
    dias = (fin - inicio).days
    for i in range(100):
        fecha = inicio + timedelta(days=random.randint(0, dias))
        personas.append({
            'id': i + 1,
            'nombre': nombres[i] if i < len(nombres) else f'Persona {i+1}',
            'fecha_nacimiento': fecha.date()
        })
    return personas

def demo():
    personas = generar_personas()
    print(f"Búsqueda Recursiva ({len(personas)} personas)")
    print("\nBuscar nombres con 'A':")
    resultados = buscar_por_nombre_inicial(personas, 'A')
    for p in resultados:
        print(f"  {p['nombre']} (ID: {p['id']})")
    print(f"\nBuscar nacidos antes de 1960:")
    resultados = buscar_por_fecha_nacimiento(personas, '1960-01-01')
    for p in resultados:
        print(f"  {p['nombre']} ({p['fecha_nacimiento']})")
    print()

if __name__ == "__main__":
    demo()
