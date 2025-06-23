import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    """
    Carrega as tarefas do arquivo JSON.
    Retorna:
        list: Lista de tarefas (cada tarefa é um dicionário).
    Se o arquivo não existir ou estiver vazio, retorna uma lista vazia.
    """
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_tarefas(tarefas):
    """
    Salva a lista de tarefas no arquivo JSON.
    Args:
        tarefas (list): Lista de tarefas a ser salva.
    """
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=2)

def listar_tarefas():
    """
    Exibe todas as tarefas cadastradas no sistema.
    Mostra o ID, título e prioridade de cada tarefa.
    """
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    for t in tarefas:
        print(f"{t['id']} - {t['titulo']} ({t['prioridade']})")

def criar_tarefa(titulo, prioridade):
    """
    Cria uma nova tarefa com título e prioridade informados.
    Args:
        titulo (str): Título da tarefa.
        prioridade (str): Prioridade da tarefa ('baixa', 'média' ou 'alta').
    """
    if prioridade not in ["baixa", "média", "alta"]:
        print("❌ Prioridade inválida! Use: baixa, média ou alta.")
        return
    if not titulo.strip():
        print("❌ O título não pode ser vazio.")
        return
    tarefas = carregar_tarefas()
    nova = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "prioridade": prioridade
    }
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    print("✅ Tarefa criada com sucesso!")

def atualizar_tarefa(id, novo_titulo):
    """
    Atualiza o título de uma tarefa pelo ID informado.
    Args:
        id (int): ID da tarefa a ser atualizada.
        novo_titulo (str): Novo título para a tarefa.
    """
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == id:
            t["titulo"] = novo_titulo
            salvar_tarefas(tarefas)
            print("✅ Tarefa atualizada!")
            return
    print("❌ ID não encontrado.")

def deletar_tarefa(id):
    """
    Remove uma tarefa do sistema pelo ID informado.
    Args:
        id (int): ID da tarefa a ser removida.
    """
    tarefas = carregar_tarefas()
    novas_tarefas = [t for t in tarefas if t["id"] != id]
    if len(novas_tarefas) == len(tarefas):
        print("❌ ID não encontrado.")
    else:
        salvar_tarefas(novas_tarefas)
        print("🗑️ Tarefa deletada!")

def filtrar_tarefas_por_prioridade(prioridade):
    """
    Exibe tarefas filtrando por prioridade ('baixa', 'média' ou 'alta').
    Args:
        prioridade (str): Prioridade para filtrar as tarefas.
    """
    tarefas = carregar_tarefas()
    filtradas = [t for t in tarefas if t["prioridade"] == prioridade]
    if not filtradas:
        print(f"Nenhuma tarefa com prioridade '{prioridade}'.")
    for t in filtradas:
        print(f"{t['id']} - {t['titulo']} ({t['prioridade']})")
