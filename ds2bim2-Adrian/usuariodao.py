from usuario import Usuario
from psycopg2 import connect
from dao import DAO

class UsuarioDao(DAO):
    def __init__(self):
        super().__init__()
    
    def buscar(self, usuario):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * from "usuario" WHERE senha = md5(%s) AND login = %s',[usuario.senha,usuario.login])
            linha = cur.fetchone()
            if(linha == None):
                return None
            else:
                User = Usuario(cod = linha[0], nome = linha[1], login =linha[2], senha = linha[3])
                return User
            conn.commit()
            cur.close()

#dao = UsuarioDao()
#usuario = Usuario(cod = 1, login = "perdeCarros", senha="vouDeMoto")
#b = dao.buscar(usuario)
#print(b)