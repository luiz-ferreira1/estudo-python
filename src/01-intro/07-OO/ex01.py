class Aluno:
    def __init__(self, origem):
        if origem is None:
            raise ValueError("Origem não pode ser nula")

        partes = origem.strip().split(",")

        if len(partes) != 3:
            raise ValueError("Formato inválido. Use: prontuario,nome,email")

        self.prontuario = partes[0].strip()
        self.nome = partes[1].strip()
        self.email = partes[2].strip()

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor):
        if valor is None or valor.strip() == "":
            raise ValueError("Prontuário não pode ser vazio ou nulo")
        self._prontuario = valor.strip()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if valor is None or valor.strip() == "":
            raise ValueError("Nome não pode ser vazio ou nulo")
        self._nome = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if valor is None or valor.strip() == "":
            raise ValueError("Email não pode ser vazio ou nulo")
        self._email = valor.strip()

    def __eq__(self, other):
        if not isinstance(other, Aluno):
            return False
        return self.prontuario == other.prontuario

    def __hash__(self):
        return hash(self.prontuario)

    def __repr__(self):
        return f"Aluno(prontuario='{self.prontuario}', nome='{self.nome}', email='{self.email}')"
