# 📌 Sistema Ágil de Gerenciamento de Tarefas - TechFlow Solutions

## 🎯 Objetivo
Desenvolver um sistema de gerenciamento de tarefas com base em metodologias ágeis, permitindo acompanhar o fluxo de trabalho, monitorar o desempenho da equipe e facilitar a priorização de tarefas críticas.

## 🛠️ Metodologia
Utilizamos **Kanban** com o GitHub Projects:
- Colunas: A Fazer | Em Progresso | Concluído

## 💻 Funcionalidade
Sistema CRUD de tarefas:
- Criar, Listar, Atualizar e Excluir tarefas.
- Armazenamento local em arquivo JSON.

## 📐 Tecnologias Utilizadas
- Python 3
- Testes com `pytest`
- Integração contínua com GitHub Actions

## 🚀 Como executar

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

2. Execute o sistema:
   ```
   python main.py
   ```

3. Para rodar os testes:
   ```
   pytest
   ```

3. Siga o menu interativo para gerenciar suas tarefas.

## 📋 Requisitos do Sistema

### Requisitos Funcionais
- O sistema deve permitir criar, listar, atualizar e excluir tarefas.
- O sistema deve armazenar as tarefas em um arquivo JSON local.
- O sistema deve permitir filtrar tarefas por prioridade.

### Requisitos Não Funcionais
- O sistema deve ser simples de usar via terminal.
- O código deve ser documentado e de fácil manutenção.
- O sistema deve ser executável em qualquer ambiente com Python 3 instalado.

## 🔄 Mudança de Escopo

Durante o desenvolvimento, o cliente solicitou a inclusão de um filtro de tarefas por prioridade para facilitar a visualização das tarefas mais críticas. Por isso, foi adicionada a funcionalidade de filtrar tarefas por prioridade no sistema.

## 📊 Diagramas UML

### Casos de Uso
![Casos de Uso](docs/uml/Diagrama%20de%20Casos%20de%20Uso.drawio.png)

### Diagrama de Classes
![Diagrama de Classes](docs/uml/Diagrama%20de%20Classes.drawio.png)

## 💻 Exemplo de uso

Ao rodar o sistema, você verá o menu:

```
📋 MENU
1. Listar tarefas
2. Criar nova tarefa
3. Atualizar tarefa
4. Deletar tarefa
5. Filtrar por prioridade
0. Sair
```
