import random

# Função para calcular os dígitos verificadores
def calcular_digito(cpf_base):
    peso = len(cpf_base) + 1
    soma = sum(int(digito) * (peso - indice) for indice, digito in enumerate(cpf_base))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

# Função para gerar o CPF completo
def gerar_cpf():
    # Gerar os 9 primeiros dígitos aleatórios
    cpf_base = ''.join(str(random.randint(0, 9)) for _ in range(9))
    
    # Calcular os dois dígitos verificadores
    primeiro_digito = calcular_digito(cpf_base)
    segundo_digito = calcular_digito(cpf_base + str(primeiro_digito))
    
    # Retornar o CPF completo
    return cpf_base + str(primeiro_digito) + str(segundo_digito)

# Função para formatar o CPF
def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# Gerar e exibir o CPF
cpf = gerar_cpf()
cpf_formatado = formatar_cpf(cpf)
print("CPF Gerado:", cpf_formatado)