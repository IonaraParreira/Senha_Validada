import re

print("--- SISTEMA DE SEGURANÇA: CADASTRO DE CREDENCIAIS ---")

# 1. Recebe a senha que o usuário digitou
senha = input("Digite uma senha para cadastro (mínimo 6 caracteres): ")

# 2. Define a regra de segurança (Regex):
# ^ indica o início da senha
# . significa que aceita qualquer caractere (letras, números ou símbolos)
# {6,} exige que a senha tenha no mínimo 6 caracteres
# $ indica o fim da senha
padrao_seguro = r"^.{6,}$"

# 3. Verifica se a senha cumpre a regra do padrão seguro
if re.fullmatch(padrao_seguro, senha):
    print("\n[SUCESSO] Senha validada com sucesso!")
    
    # 4. Mecanismo de Mascaramento:
    # Conta o tamanho da senha e substitui as letras por "*" para proteger a tela
    senha_escondida = "*" * len(senha)
    print(f"Sua senha foi mascarada para segurança: {senha_escondida}")

else:
    print("\n[ERRO] Senha inválida!")
    print("Atenção: A senha precisa ter pelo menos 6 caracteres para ser segura.")