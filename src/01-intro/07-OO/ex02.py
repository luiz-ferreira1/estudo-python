class Projeto:
    def __init__(self, origem):
        """
        Constrói um Projeto a partir de uma string no formato:
        'codigo,titulo,responsavel'
        Ex: '1,Laboratório de Desenvolvimento de Software,Pedro Gomes'
        """
        if origem is None:
            raise ValueError("Origem não pode ser nula")

        partes = origem.strip().split(",")

        if len(partes) != 3:
            raise ValueError(
                "Formato inválido. Use: codigo,titulo,responsavel")

        self.codigo = partes[0].strip()
        self.titulo = partes[1].strip()
        self.responsavel = partes[2].strip()

    # ---------- codigo ----------
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None or str(valor).strip() == "":
            raise ValueError("Código não pode ser vazio ou nulo")

        try:
            valor_int = int(valor)
        except ValueError:
            raise ValueError("Código deve ser um número inteiro")

        self._codigo = valor_int

    # ---------- titulo ----------
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if valor is None or valor.strip() == "":
            raise ValueError("Título não pode ser vazio ou nulo")
        self._titulo = valor.strip()

    # ---------- responsavel ----------
    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if valor is None or valor.strip() == "":
            raise ValueError("Responsável não pode ser vazio ou nulo")
        self._responsavel = valor.strip()

    # ---------- comparação ----------
    def __eq__(self, other):
        if not isinstance(other, Projeto):
            return False
        return self.codigo == other.codigo

    def __repr__(self):
        return f"Projeto(codigo={self.codigo}, titulo='{self.titulo}', responsavel='{self.responsavel}')"
