import os
import json
def load_tasks():
    try:
        with open('tarefas.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não existir
def save_tasks(tarefas):
    with open('tarefas.json', 'w') as file:
        json.dump(tarefas, file, indent=4)  # Salva a lista de tarefas no arquivo JSON
def add_task(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    if not descricao.strip():
        print("Descrição da tarefa não pode ser vazia.")
        return
    prioridade = input("Digite a prioridade da tarefa (alta, média, baixa): ").lower()
    if prioridade not in ['alta', 'média', 'baixa']:
        print("Prioridade inválida. Use 'alta', 'média' ou 'baixa'.")
        return
    tarefa = {'descricao': descricao,'prioridade': prioridade, 'concluida': False}
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")
def list_tasks(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            if tarefa['concluida']:
                print(f"{i}. {tarefa['descricao']} - {status}")
            else:
                print(f"{i}. {tarefa['descricao']} - {status} - {tarefa['prioridade']}")
def edit_descripition_tesk(tarefas, index):
    if 0 <= index < len(tarefas):
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        tarefas[index]['descricao'] = nova_descricao
        print(f"Tarefa editada para '{nova_descricao}' com sucesso!")
    else:
        print("Índice inválido. Tente novamente.")
def edit_prioriti_tesk(tarefas, index):
    if 0 <= index < len(tarefas):
        nova_prioridade = input("Digite a nova prioridade da tarefa (alta, média, baixa): ").lower()
        tarefas[index]['prioridade'] = nova_prioridade
        print(f"Tarefa editada para '{nova_prioridade}' com sucesso!")
    else:
        print("Índice inválido. Tente novamente.")
def mark_task_as_completed(tarefas, index):
    if 0 <= index < len(tarefas):
        tarefas[index]['concluida'] = True
        tarefas[index]['prioridade'] = 'none' 
        print(f"Tarefa '{tarefas[index]['descricao']}' marcada como concluída.")
    else:
        print("Índice inválido. Tente novamente.")
def remove_task(tarefas, index):
    if 0 <= index < len(tarefas):
        removed_task = tarefas.pop(index)
        print(f"Tarefa '{removed_task['descricao']}' removida com sucesso.")
    else:
        print("Índice inválido. Tente novamente.")  


def main():

    

    
    tarefas = load_tasks()  # Lista para armazenar as tarefas
    print("Bem-vindo ao gerenciador de tarefas!")
    run = False

    while run:
        try:
            i = int(input("1. Adicionar tarefa\n2. Listar tarefas\n3. Marcar como concluída\n4. Remover tarefa\n5. editar tarefa\n6. Sair\nEscolha uma opção: "))
            
            if i == 1:
                os.system('cls')  # Limpa a tela no Windows
                print("Adicionar tarefa")
                add_task(tarefas)
                save_tasks(tarefas)
            elif i == 2:
                os.system('cls')
                print("Listar tarefas")
                list_tasks(tarefas)
                # Lógica para listar tarefas
            elif i == 3:
                os.system('cls')
                print("Marcar como concluída")
                list_tasks(tarefas)  # Exibe a lista de tarefas antes de marcar como concluída
                index = int(input("Digite o índice da tarefa a ser marcada como concluída: ")) - 1
                mark_task_as_completed(tarefas, index)
                save_tasks(tarefas)
                # Lógica para marcar tarefa como concluída
            elif i == 4:
                os.system('cls')
                print("Remover tarefa")
                list_tasks(tarefas) # Exibe a lista de tarefas antes de remover
                index = int(input("Digite o índice da tarefa a ser removida: ")) - 1
                confirm = input("Tem certeza que deseja remover esta tarefa? (s/n): ").lower()
                if confirm == 's':
                    remove_task(tarefas, index)
                    save_tasks(tarefas)
                else:
                    print("Operação cancelada.")
                # Lógica para remover tarefa
            elif i == 5:
                os.system('cls')
                print("Editar tarefa")
                list_tasks(tarefas)
                index = int(input("Digite o índice da tarefa a ser editada: ")) - 1
                confirm = input("Tem certeza que deseja editar esta tarefa? (s/n): ").lower()
                if confirm == 's':
                    edit_option = int(input("Escolha a opção de edição:\n1. Editar descrição\n2. Editar prioridade\nEscolha uma opção: "))
                    if edit_option == 1:
                        edit_descripition_tesk(tarefas, index)
                    elif edit_option == 2:
                        edit_prioriti_tesk(tarefas, index)
                    else:
                        print("Opção inválida.")
                    save_tasks(tarefas)
                else:
                    print("Operação cancelada.")
            elif i == 6:
                confirm = input("Tem certeza que deseja sair? (s/n): ").lower()
                if confirm == 's':
                    os.system('cls')
                    print("Saindo...")
                    save_tasks(tarefas)
                    run = False
                else:
                    print("Operação cancelada.")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

# Chamada da função principal
if __name__ == "__main__":
    main()
    