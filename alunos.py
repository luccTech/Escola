import dados

def gerar_id():
    if len(dados.alunos) == 0:
        return 1
    ultimo_id = dados.alunos[-1]["id"]
    return ultimo_id + 1

def listar_alunos():
    if len(dados.alunos) == 0:
        print("\n\033[93m[!] Nenhum aluno cadastrado no sistema.\033[0m")
        return

    print("\033[1;94m" + "="*60 + "\033[0m")
    print(f"\033[1m{'ID':<4} {'NOME':<22} {'CPF':<16} {'TURMA':<6}\033[0m")
    print("\033[94m" + "-"*60 + "\033[0m")

    for aluno in dados.alunos:
        print(f"{aluno['id']:<4} {aluno['nome']:<22} {aluno['cpf']:<16} {aluno['turma']:<6}")
    
    print("\033[94m" + "="*60 + "\033[0m")

def cadastrar_aluno():
    print("\033[94m==================================================\033[0m")
    print("\033[1;94m               CADASTRAR NOVO ALUNO               \033[0m")
    print("\033[94m==================================================\033[0m")
    
    nome = input(" Nome Completo: ")
    cpf = input(" CPF: ")
    turma = input(" Turma: ")

    dados.alunos.append({
        "id": gerar_id(),
        "nome": nome,
        "cpf": cpf,
        "turma": turma,
        "nota": 0.0,
        "frequencia": 100.0
    })

    print("\n\033[92m[OK] Aluno cadastrado com sucesso!\033[0m")

def editar_aluno():
    print("\033[1;94m               EDITAR DADOS DE ALUNO              \033[0m")
    listar_alunos()
    
    try:
        id_aluno = int(input("\nDigite o ID do aluno que deseja editar: "))
    except ValueError:
        print("\033[91mID inválido.\033[0m")
        return

    for aluno in dados.alunos:
        if aluno["id"] == id_aluno:
            print(f"\nEditando dados de: \033[1m{aluno['nome']}\033[0m")
            print("-" * 30)
            aluno["nome"] = input(" Novo nome: ")
            aluno["cpf"] = input(" Novo CPF: ")
            aluno["turma"] = input(" Nova turma: ")
            print("\n\033[92m[OK] Dados atualizados com sucesso!\033[0m")
            return

    print("\033[91m[X] Aluno não encontrado.\033[0m")

def excluir_aluno():
    print("\033[1;91m               REMOVER ALUNO DO SISTEMA           \033[0m")
    listar_alunos()
    
    try:
        id_aluno = int(input("\nDigite o ID do aluno que deseja EXCLUIR: "))
    except ValueError:
        print("\033[91mID inválido.\033[0m")
        return

    for aluno in dados.alunos:
        if aluno["id"] == id_aluno:
            dados.alunos.remove(aluno)
            print("\n\033[92m[OK] Aluno removido com sucesso!\033[0m")
            return

    print("\033[91m[X] Aluno não encontrado.\033[0m")