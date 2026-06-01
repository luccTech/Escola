import dados

def contar_alunos_risco():
    total = 0
    for aluno in dados.alunos:
        if aluno["nota"] < 6 or aluno["frequencia"] < 75:
            total += 1
    return total

def mostrar_alertas():
    print("\033[1;91m==================================================\033[0m")
    print("\033[1;91m             PAINEL DE ALERTAS CRÍTICOS           \033[0m")
    print("\033[1;91m==================================================\033[0m")

    encontrou = False

    for aluno in dados.alunos:
        if aluno["nota"] < 6 or aluno["frequencia"] < 75:
            encontrou = True

            if aluno["nota"] < 4 and aluno["frequencia"] < 60:
                tag_status = "\033[1;41m RISCO CRÍTICO \033[0m"
            elif aluno["nota"] < 6 and aluno["frequencia"] < 75:
                tag_status = "\033[1;31m RISCO DUPLO \033[0m"
            elif aluno["nota"] < 6:
                tag_status = "\033[91m RISCO POR NOTA \033[0m"
            elif aluno["frequencia"] < 75:
                tag_status = "\033[93m RISCO POR FREQUÊNCIA \033[0m"

            print(f" ID: {aluno['id']:<3} | Aluno: {aluno['nome']:<20} | Status: {tag_status}")
            print(f"       Nota: {aluno['nota']:.1f}  -  Frequência: {aluno['frequencia']:.0f}%")
            print("\033[91m" + "-"*50 + "\033[0m")

    if not encontrou:
        print("\n\033[92m[✓] Excelente! Nenhum aluno em situação de risco.\033[0m\n")