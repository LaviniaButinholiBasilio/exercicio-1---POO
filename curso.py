class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = []

    def adicionar_turma(self, turma):
        if turma not in self.turmas:
            self.turmas.append(turma)

    def excluir_turma(self, turma):
        if turma in self.turmas:
            self.turmas.remove(turma)

    def obter_nomes_alunos(self):
        alunos = set()
        for turma in self.turmas:
            alunos.update(turma.obter_nomes_alunos())
        return list(alunos)

    def obter_nomes_professores(self):
        professores = set()
        for turma in self.turmas:
            professores.add(turma.obter_nome_professor())
        return list(professores)

    def obter_disciplinas(self):
        disciplinas = set()
        for turma in self.turmas:
            disciplinas.add(turma.disciplina.nome)
        return list(disciplinas)

    def verificar_aluno_no_curso(self, aluno):
        return any(turma.verificar_aluno_na_turma(aluno) for turma in self.turmas)

    def excluir_aluno_do_curso(self, aluno):
        for turma in self.turmas:
            turma.excluir_aluno(aluno)
