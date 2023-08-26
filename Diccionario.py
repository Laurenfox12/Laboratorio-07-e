persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True, #
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}
if "skills" in persona:
    habilidad = persona['skills']
    cantidad_habilidades = len(habilidad)
    if cantidad_habilidades > 0:
        habilidad_medio = habilidad[cantidad_habilidades // 2]
        print("Habilidad del medio:", habilidad_medio)
else: print("No existe la clave skills en el diccionario")
if "skills" in persona:
    if "Python" in persona['skills']:
        print("La persona tiene la habilidad Python")
    else:print("La persona no cuenta con la habilidad Python")
else: print("No existe la clave skills en el diccionario")
if "skills" in persona:
    habilidades = persona['skills']
    if "JavaScript" in habilidades and "React" in habilidades:print("El es un desarrollador fronted")
    elif "Node" in habilidades and "Python" in habilidades and "MongoDB" in habilidades:print("El es un dsarrollador backend")
    elif "React" in habilidades and "Node" in habilidades and "MongoDB" in habilidades:print("El es un desarrollador fullstack")
    else: print("Título desconocido")