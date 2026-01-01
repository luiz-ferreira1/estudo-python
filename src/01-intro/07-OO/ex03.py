from aluno import Aluno
from projeto import Projeto


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        """
        codigo: int
        data_inicio: str (ex: '2025-03-01')
        data_fim: str (ex: '2025-06-30')
        aluno: objeto Aluno
        projeto: objeto Projeto
        """
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    # ---------- codigo ----------
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None or str(valor).strip() == "":
            raise ValueError(
                "Código da participação não pode ser vazio ou nulo")
        try:
            self._codigo = int(valor)
        except ValueError:
            raise ValueError("Código da participação deve ser inteiro")

    # ---------- data_inicio ----------
    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):
        if valor is None or valor.strip() == "":
            raise ValueError("Data de início não pode ser vazia ou nula")
        self._data_inicio = valor.strip()

    # ---------- data_fim ----------
    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, valor):
        if valor is None or valor.strip() == "":
            raise ValueError("Data de fim não pode ser vazia ou nula")
        self._data_fim = valor.strip()

    # ---------- aluno ----------
    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, valor):
        if valor is None or not isinstance(valor, Aluno):
            raise ValueError("Aluno deve ser um objeto da classe Aluno")
        self._aluno = valor

    # ---------- projeto ----------
    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, valor):
        if valor is None or not isinstance(valor, Projeto):
            raise ValueError("Projeto deve ser um objeto da classe Projeto")
        self._projeto = valor

    # ---------- comparação ----------
    def __eq__(self, other):
        if not isinstance(other, Participacao):
            return False
        return self.codigo == other.codigo

    def __repr__(self):
        return (f"Participacao(codigo={self.codigo}, data_inicio='{self.data_inicio}', "
                f"data_fim='{self.data_fim}', aluno={self.aluno}, projeto={self.projeto})")
