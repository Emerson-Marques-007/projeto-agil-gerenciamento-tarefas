from tarefa_service import *

def menu():
    while True:
        print("\n📋 MENU")
        print("1. Listar tarefas")
        print("2. Criar nova tarefa")
        print("3. Atualizar tarefa")
        print("4. Deletar tarefa")
        print("5. Filtrar por prioridade")
        print("0. Sair")
        op = input("Escolha: ")

        if op == "1":
            listar_tarefas()
        elif op == "2":
            titulo = input("Título: ")
            prioridade = input("Prioridade (baixa/média/alta): ")
            criar_tarefa(titulo, prioridade)
        elif op == "3":
            try:
                id = int(input("ID da tarefa: "))
                titulo = input("Novo título: ")
                atualizar_tarefa(id, titulo)
            except ValueError:
                print("❌ Digite um número válido para o ID!")
        elif op == "4":
            try:
                id = int(input("ID da tarefa: "))
                deletar_tarefa(id)
            except ValueError:
                print("❌ Digite um número válido para o ID!")
        elif op == "5":
            prioridade = input("Filtrar por (baixa/média/alta): ")
            filtrar_tarefas_por_prioridade(prioridade)
        elif op == "0":
            print("Saindo...")
            break

menu()
