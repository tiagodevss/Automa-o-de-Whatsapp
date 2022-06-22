import pymysql

def conectar():
    conexão = pymysql.connect(
        host = "",
        user = "",
        password = "",
        database = "",
        autocommit = True
    )
    cursor = conexão.cursor()
    return cursor
    
def buscar(cursor):
    try:
        cursor.execute("SELECT * FROM ___ WHERE PrimeiroContato = 'Não'")
        resultadoDados = cursor.fetchone()
        Whatsapp = resultadoDados[2]

        return Whatsapp
    except:
        print('A lista foi finalizada')
        quit()