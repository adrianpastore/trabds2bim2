class Ideia:
    def __init__(self,**kwargs):
        if(kwargs.get("cod")): self._cod = kwargs["cod"]
        if(kwargs.get("datahoraatualizacao")): self._datahoraatualizacao = kwargs["datahoraatualizacao"]
        if(kwargs.get("titulo")): self._titulo = kwargs["titulo"]
        if(kwargs.get("descricao")): self._descricao = kwargs["descricao"]
        if(kwargs.get("usuario")): self._usuario = kwargs["usuario"]
   
    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self,titulo):
        self._titulo = titulo
    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self,descricao):
        self._descricao = descricao

    @property
    def cod(self):
        return self._cod
    @cod.setter
    def cod(self,cod):
        self._cod = cod
    @property
    def datahoraatualizacao(self):
        return self._datahoraatualizacao
    @datahoraatualizacao.setter
    def datahoraatualizacao(self,datahoraatualizacao):
        self._datahoraatualizacao = datahoraatualizacao

    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self,usuario):
        self._usuario = usuario

    def persistido(self):
        return hasattr(self,"_cod") and self.cod!=None 

from usuario import Usuario
u = Usuario(nome="julio",login="juju", senha='hehe', cod=1)

i = Ideia(usuario=u,cod=1,titulo="teste", descricao='desc')
print(i)