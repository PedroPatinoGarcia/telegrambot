import pymysql

def establecer_conexion():
    conexion = pymysql.connect(host='193.144.42.124', port=33306, user='Pedro', password='1Super-Password', database='inferno')
    return conexion

def destino(name):
    try:
        conexion = establecer_conexion()

        with conexion.cursor() as cursor:
            cursor.execute(f"SELECT nivel, nome_nivel FROM admision WHERE nome LIKE '{name}'")
            result = cursor.fetchone()

        if result:
            nivel, nome_nivel = result
            return f'Estoy en el {nivel}ª nivel. El pecado "{nome_nivel}"'
        else:
            return 'No se encontraron resultados para el nombre proporcionado.'
    except Exception as e:
        return f'Error: {e}'
    finally:
        if conexion:
            conexion.close()   