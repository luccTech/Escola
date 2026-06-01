import dados

def listar_notas():
    if len(dados.alunos) == 0:
        print("\n\033[93m[!] Nenhum aluno cadastrado para exibir notas.\033[0m")
        return

    print("\033[1;94m" + "="*55 + "\033[0m")
    print(f"\033[1m{'ID':<4} {'NOME':<22} {'NOTA':<8} {'FREQUÊNCIA':<10}\033[0m")
    print("\033[94m" + "-"*55 + "\033[0m")

    for aluno in dados.alunos:
        print(f"{aluno['id']:<4} {aluno['nome']:<22} {aluno['nota']:<8.1f} {aluno['frequencia']:>3.0f}%")
    
    print("\033[94m" + "="*55 + "\033[0m")

def lancar_nota_frequencia():
    print("\033[1;94m               LANÇAMENTO DE NOTAS E FREQUÊNCIA   \033[0m")
    listar_notas()

    try:
        id_aluno = int(input("\nDigite o ID do aluno: "))
    except ValueError:
        print("\033[91mID inválido.\033[0m")
        return

    for aluno in dados.alunos:
        if aluno["id"] == id_aluno:
            print(f"\nAluno Selecionado: \033[1m{aluno['nome']}\033[0m")
            print(" [1] Alterar Nota Atual")
            print(" [2] Alterar Frequência Atual")
            op = input(" Escolha: ")

            if op == "1":
                try:
                    aluno["nota"] = float(input(" Nova nota (0-10): "))
                    print("\033[92m[OK] Nota atualizada!\033[0m")
                except ValueError:
                    print("\033[91mValor incorreto para nota.\033[0m")
            elif op == "2":
                try:
                    aluno["frequencia"] = float(input(" Nova frequência (0-100): "))
                    print("\033[92m[OK] Frequência atualizada!\033[0m")
                except ValueError:
                    print("\033[91mValor incorreto para frequência.\033[0m")
            return

    print("\033[91m[X] Aluno não encontrado.\033[0m")