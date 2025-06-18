import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    """Carrega a lista de tarefas do arquivo JSON. Retorna uma lista de dicionários."""
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=2)

def listar_tarefas():
    """Exibe todas as tarefas cadastradas no sistema."""
    tarefas = carregar_tarefas()
    for t in tarefas:
        print(f"{t['id']} - {t['titulo']} ({t['prioridade']})")

def criar_tarefa(titulo, prioridade):
    """Cria uma nova tarefa com título e prioridade informados."""
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
    """Atualiza o título de uma tarefa pelo ID informado."""
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == id:
            t["titulo"] = novo_titulo
            break
    salvar_tarefas(tarefas)
    print("✅ Tarefa atualizada!")

def deletar_tarefa(id):
    """Remove uma tarefa do sistema pelo ID informado."""
    tarefas = carregar_tarefas()
    tarefas = [t for t in tarefas if t["id"] != id]
    salvar_tarefas(tarefas)
    print("🗑️ Tarefa deletada!")

def filtrar_tarefas_por_prioridade(prioridade):
    """Exibe tarefas filtrando por prioridade (baixa, média ou alta)."""
    tarefas = carregar_tarefas()
    filtradas = [t for t in tarefas if t["prioridade"] == prioridade]
    for t in filtradas:
        print(f"{t['id']} - {t['titulo']} ({t['prioridade']})")
