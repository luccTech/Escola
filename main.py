import alunos
import notas
import alertas
import dados
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

sistema_ativo = True

while sistema_ativo:
    limpar_tela()
    total_alunos = len(dados.alunos)
    total_risco = alertas.contar_alunos_risco()

    print("\033[94m==================================================\033[0m")
    print("\033[1;94m                SISTEMA ESCOLA++                  \033[0m")
    print("\033[94m==================================================\033[0m")
    print(f" Status do Sistema: \033[92mAtivo\033[0m | Total Alunos: \033[96m{total_alunos}\033[0m")
    print(f" Alunos em Situação de Risco: \033[91m{total_risco}\033[0m")
    print("\033[94m==================================================\033[0m")
    print(" [1] Gerenciar Alunos")
    print(" [2] Gerenciar Notas e Frequência")
    print(" [3] Ver Alertas Críticos")
    print(" [0] Sair do Sistema")
    print("\033[94m--------------------------------------------------\033[0m")

    op = input("Selecione uma opção: ")

    if op == "1":
        gerenciar = True
        while gerenciar:
            limpar_tela()
            print("\033[94m==================================================\033[0m")
            print("\033[1;94m               GERENCIAR ALUNOS                   \033[0m")
            print("\033[94m==================================================\033[0m")
            print(" [1] Listar Alunos Cadastrados")
            print(" [2] Cadastrar Novo Aluno")
            print(" [3] Editar Dados de Aluno")
            print(" [4] Excluir Aluno do Sistema")
            print(" [0] Voltar ao Menu Principal")
            print("\033[94m--------------------------------------------------\033[0m")

            escolha = input("Selecione uma opção: ")

            if escolha == "1":
                limpar_tela()
                alunos.listar_alunos()
                input("\nPressione [ENTER] para voltar...")
            elif escolha == "2":
                limpar_tela()
                alunos.cadastrar_aluno()
                input("\nPressione [ENTER] para voltar...")
            elif escolha == "3":
                limpar_tela()
                alunos.editar_aluno()
                input("\nPressione [ENTER] para voltar...")
            elif escolha == "4":
                limpar_tela()
                alunos.excluir_aluno()
                input("\nPressione [ENTER] para voltar...")
            elif escolha == "0":
                gerenciar = False

    elif op == "2":
        gerenciar = True
        while gerenciar:
            limpar_tela()
            print("\033[94m==================================================\033[0m")
            print("\033[1;94m               GERENCIAR NOTAS                    \033[0m")
            print("\033[94m==================================================\033[0m")
            print(" [1] Visualizar Boletim Geral")
            print(" [2] Lançar Nota ou Frequência")
            print(" [0] Voltar ao Menu Principal")
            print("\033[94m--------------------------------------------------\033[0m")

            escolha = input("Selecione uma opção: ")

            if escolha == "1":
                limpar_tela()
                notas.listar_notas()
                input("\nPressione [ENTER] para voltar...")
            elif escolha == "2":
                limpar_tela()
                notas.lancar_nota_frequencia()
                input("\nPressione [ENTER] para voltar...")
            elif escolha == "0":
                gerenciar = False

    elif op == "3":
        limpar_tela()
        alertas.mostrar_alertas()
        input("\nPressione [ENTER] para voltar...")

    elif op == "0":
        sistema_ativo = False

limpar_tela()
print("\n\033[92mSistema encerrado com sucesso. Até logo!\033[0m\n")