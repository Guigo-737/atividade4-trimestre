import re
from geopy.distance import geodesic

# Função para calcular o total das compras
def calcular_total_compras(compras):
    total = sum(compras)
    return total

# Função para calcular a distância total entre as coordenadas em Brasília
def calcular_distancia_coordenadas(coordenadas_basilia):
    if len(coordenadas_basilia) < 2:
        return 0
    inicio = coordenadas_basilia[0]
    fim = coordenadas_basilia[-1]
    distancia = geodesic(inicio, fim).kilometers
    return distancia

# Função para validar CPFs
def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  # Remove tudo o que não for número
    if len(cpf) != 11:
        return False
    # Algoritmo básico de validação
    def calcular_digito(cpf, peso):
        soma = sum(int(digit) * peso for digit, peso in zip(cpf[:9], peso))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    peso1 = list(range(10, 1, -1))
    peso2 = list(range(11, 2, -1))

    digito1 = calcular_digito(cpf, peso1)
    digito2 = calcular_digito(cpf + str(digito1), peso2)

    return cpf[-2:] == f'{digito1}{digito2}'

# Função para calcular a média das notas
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    media = sum(notas) / len(notas)
    return media

# Função para marcar tarefas como concluídas
def concluir_tarefa(tarefas, tarefa_concluida):
    if tarefa_concluida in tarefas:
        tarefas[tarefa_concluida] = "Concluída"
        return f"Tarefa '{tarefa_concluida}' concluída!"
    return "Tarefa não encontrada."

# Função para listar todos os meses do ano
def listar_meses():
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses

# Função para adicionar um aluno
def adicionar_aluno(alunos, nome, idade, curso):
    aluno = {"nome": nome, "idade": idade, "curso": curso}
    alunos.append(aluno)
    return alunos

# Exemplo de uso das funções

# Dados de exemplo
compras = [100, 250, 80, 40, 300]
coordenadas_basilia = [(15.7801, -47.9292), (15.7831, -47.9242)]  # Coordenadas fictícias
cpfs = ["123.456.789-09", "987.654.321-00"]
notas = [7.5, 8.0, 6.5, 9.0]
tarefas = {"Lavar a louça": "Pendente", "Estudar para prova": "Pendente"}
meses = listar_meses()
alunos = [{"nome": "João", "idade": 20, "curso": "Engenharia"}]

# Testando as funções
print("Total das compras:", calcular_total_compras(compras))
print("Distância entre as coordenadas em Brasília:", calcular_distancia_coordenadas(coordenadas_basilia), "km")
print("CPF válido?", validar_cpf(cpfs[0]))
print("Média das notas:", calcular_media(notas))
print(concluir_tarefa(tarefas, "Lavar a louça"))
print("Meses do ano:", meses)
alunos = adicionar_aluno(alunos, "Maria", 22, "Medicina")
print("Lista de alunos:", alunos)
