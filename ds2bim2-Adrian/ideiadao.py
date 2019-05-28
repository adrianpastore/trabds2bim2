from ideia import Ideia
from usuario import Usuario
from psycopg2 import connect
from datetime import datetime
from dao import DAO

class IdeiaDao(DAO):
    def __init__(self):
        super().__init__()
    
    def excluir(self, ideia):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM ideia WHERE cod=%s",[ideia.cod])
                conn.commit()
                cur.close()
                ideia.cod=None
        except BaseException as e:
            print ("Problema na exclusão -- exception seguindo para ser tratada")
            raise e
    def buscar(self, cod):
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT i."cod", i."titulo", i."descricao", i."datahoraatualizacao",\
                    u."cod",u."nome", u."login" FROM "ideia" i LEFT JOIN "usuario" u \
                        ON u."cod" = i."codusuario" WHERE i."cod"=%s', [cod])
                row = cur.fetchone()
                u = Usuario(cod=row[4], nome=row[5], login=row[6])
                ideia =Ideia(usuario=u, cod=row[0], titulo=row[1], descricao=row[2], \
                    datahoraatualizacao=row[3])
                conn.commit()
                cur.close()
                return ideia
        except BaseException as e:
            print ("Problema no buscar -- exception seguindo para ser tratada")
            raise e    
    def listar(self, limit, offset):
        vet = []
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute('SELECT "cod", "titulo", "descricao", "datahoraatualizacao"\
                     FROM "ideia" LIMIT %s OFFSET %s',[limit, offset])
                for row in cur.fetchall():
                    vet.append(Ideia(cod=row[0],titulo=row[1],descricao = row[2],\
                        datahoraatualizacao=row[3]))
                cur.close()
        except BaseException as e:
            print ("Problema no listar -- exception seguindo para ser tratada")
            raise e    
        return vet

    def inserir(self, ideia):
        params =  [ideia.titulo, ideia.descricao, ideia.usuario.cod]
        query = "INSERT INTO ideia (titulo, descricao, codusuario, datahoraatualizacao) \
            VALUES (%s, %s, %s, now()) RETURNING cod, datahoraatualizacao"
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute(query, params)
                row = cur.fetchone()
                ideia.cod = row[0]
                ideia.datahoraatualizacao = row[1]
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no inserir -- exception seguindo para ser tratada")
            raise e

    def alterar(self, ideia):
        params =  [ideia.titulo, ideia.descricao, ideia.usuario.cod, ideia.cod, ideia.datahoraatualizacao]
        query = "UPDATE ideia SET titulo=%s, descricao=%s, codusuario=%s, \
                datahoraatualizacao=now() WHERE cod = %s AND datahoraatualizacao = %s \
                    RETURNING datahoraatualizacao"
        try: 
            with connect(self._dados_con) as conn:
                cur = conn.cursor()
                cur.execute(query, params)
                row = cur.fetchone()
                ideia.datahoraatualizacao = row[0]
                conn.commit()
                cur.close()
        except BaseException as e:
            print ("Problema no alterar -- exception seguindo para ser tratada")
            raise e

    def salvar(self, ideia):
        if ideia.persistido():
            self.alterar(ideia)
        else:
            self.inserir(ideia)
        

#if __name__ == "__main__":
#    dao = IdeiaDao()
#    u = Usuario(cod=1)
#    ideia = Ideia(titulo = "deis", descricao = "mto deis", usuario=u)
#    print(ideia.persistido())
#
#    dao.salvar(ideia)
#    novo = dao.buscar(ideia.cod)
#
#    ideia.titulo="novo deis"
#    dao.salvar(ideia)
# 
#    lis = dao.listar(10,0)
#    print(ideia.persistido())
#
#    dao.excluir(ideia)
#
#    print(ideia.persistido())


    