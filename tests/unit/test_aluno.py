import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

#
def test_calcular_media():
    aluno = Aluno(nome="Ana", notas=[10, 8], faltas=0)

    assert aluno.calcular_media() == 9


def test_situacao_deve_aprovar_media_seis():
    aluno = Aluno(nome="Carlos", notas=[6, 6, 6, 6], faltas=0)

    assert aluno.situacao() == "Aprovado"


def test_situacao_deve_reprovar_media_menor_que_seis():
    aluno = Aluno(nome="Eduardo", notas=[5, 5, 5, 5], faltas=0)

    assert aluno.situacao() == "Reprovado"


def test_menor_nota_deve_retornar_menor_valor():
    aluno = Aluno(nome="Beatriz", notas=[8, 5, 10, 7], faltas=0)

    assert aluno.menor_nota() == 5


def test_calcular_media_arredondada_deve_arredondar_para_inteiro_mais_proximo():
    aluno = Aluno(nome="Daniel", notas=[7, 8, 8], faltas=0)

    assert aluno.calcular_media_arredondada() == 8


# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
