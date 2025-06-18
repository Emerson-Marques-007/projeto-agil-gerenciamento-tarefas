import os
import pytest
from tarefa_service import (
    salvar_tarefas,
    carregar_tarefas,
    criar_tarefa,
    atualizar_tarefa,
    deletar_tarefa,
    filtrar_tarefas_por_prioridade
)

ARQUIVO = "tarefas.json"

@pytest.fixture(autouse=True)
def limpar_arquivo():
    # Limpa o arquivo antes e depois de cada teste
    salvar_tarefas([])
    yield
    salvar_tarefas([])

def test_criar_tarefa_adiciona_nova_tarefa():
    criar_tarefa("Tarefa Teste", "alta")
    tarefas = carregar_tarefas()
    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Tarefa Teste"
    assert tarefas[0]["prioridade"] == "alta"

def test_listar_tarefas_exibe_todas(capsys):
    criar_tarefa("Tarefa 1", "baixa")
    criar_tarefa("Tarefa 2", "alta")
    from tarefa_service import listar_tarefas
    listar_tarefas()
    captured = capsys.readouterr()
    assert "Tarefa 1" in captured.out
    assert "Tarefa 2" in captured.out

def test_atualizar_tarefa_altera_titulo():
    criar_tarefa("Antigo", "média")
    atualizar_tarefa(1, "Novo Título")
    tarefas = carregar_tarefas()
    assert tarefas[0]["titulo"] == "Novo Título"

def test_deletar_tarefa_remove_tarefa():
    criar_tarefa("Para deletar", "baixa")
    deletar_tarefa(1)
    tarefas = carregar_tarefas()
    assert len(tarefas) == 0

def test_filtrar_tarefas_por_prioridade_exibe_corretamente(capsys):
    criar_tarefa("Alta prioridade", "alta")
    criar_tarefa("Baixa prioridade", "baixa")
    filtrar_tarefas_por_prioridade("alta")
    captured = capsys.readouterr()
    assert "Alta prioridade" in captured.out
    assert "Baixa prioridade" not in captured.out

def test_criar_e_listar():
    salvar_tarefas([])  # limpa tudo
    criar_tarefa("Testar função", "alta")
    tarefas = carregar_tarefas()
    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Testar função"
