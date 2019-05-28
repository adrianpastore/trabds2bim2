class Usuario:
    def __init__(self,**kwargs):
        if(kwargs.get("cod")): self._cod = kwargs["cod"]
        if(kwargs.get("nome")): self._nome = kwargs["nome"]
        if(kwargs.get("login")): self._login = kwargs["login"]
        if(kwargs.get("senha")): self._senha = kwargs["senha"]
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    @property
    def login(self):
        return self._login
    @login.setter
    def login(self,login):
        self._login = login

    @property
    def cod(self):
        return self._cod
    @cod.setter
    def cod(self,cod):
        self._cod = cod

    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self,senha):
        self._senha = senha

    def persistido(self):
        return hasattr(self,"_cod") and self.cod!=None