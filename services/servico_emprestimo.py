from models.emprestimo import Emprestimo


class ServicoEmprestimo:
    def registrar(self, equipamento_id: int, usuario_nome: str,
                  usuario_email: str, dias: int) -> bool:
        ...

    def devolver(self, emprestimo_id: int) -> None:
        ...

    def listar_atrasados(self) -> None:
        ...
