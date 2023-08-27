# Definir el diccionario de la persona
persona = {
    'first_name': 'Edem',
    'last_name': 'Terraza',
    'age': 31,
    'country': 'Peru',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# a) Comprobar si el diccionario de la persona tiene la clave de habilidades e imprimir la habilidad del medio

if 'skills' in persona:
    skills = persona['skills']
    indice_medio= len(skills) // 2
    habilidad_media = skills[indice_medio]
    print("Habilidad del medio:", habilidad_media)

# b) Comprobar si el diccionario de la persona tiene la clave de habilidades y si tiene una habilidad específica
if 'skills' in persona:
    skills = persona['skills']
    if 'Python' in skills:
        print("La persona tiene la habilidad 'Python'.")

# Problema c
skills = persona.get('skills', [])
if skills == ['JavaScript', 'React']:
    print("Él es un desarrollador frontend")
elif set(skills) == {'Node', 'Python', 'MongoDB'}:
    print("Él es un desarrollador backend")
elif set(skills) == {'React', 'Node', 'MongoDB'}:
    print("Él es un desarrollador fullstack")
else:
    print("Título desconocido")
