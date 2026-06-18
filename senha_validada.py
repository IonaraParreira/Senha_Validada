import re

print("\n--- SISTEMA DE SEGURANÇA: CADASTRO DE CREDENCIAIS ---\n")

# 1. Recebe a senha do usuário
senha = input("Digite sua nova senha: ")

# 2. Lista para guardar os erros encontrados
erros = []

# 3. Validação de cada requisito individualmente
if len(senha) < 8:
    erros.append("• Ter no mínimo 8 caracteres.")

if not re.search(r"\d", senha):
    erros.append("• Conter pelo menmos 1 número.")

if not re.search(r"[@$!%*?&#]", senha):
    erros.append("• Conter pelo menos 1 carcatere especial ( ex: @, $, !, %, *, ?, &, #).")

if not re.search(r"[A-Z]",senha):
    erros.append("• Conter pelo menos 1 letra maiúscula.")

if not re.search(r"[a-z]", senha):
    erros.append("• Conter pelo menos 1 letra minúscula.")

# 4. Exibe o resultado com base nos erros encontrados
if not erros:
    print("\n 🟢 Senha validada com sucesso!")

    # Mantém o mascaramento implementado
    senha_escondida = "*" * len(senha)
    print(f"Sua senha foi mascarada para sua própria segurança: {senha_escondida}")

else:
    print("\n 🔴 Senha fraca! Para torná-la segura, ajuste o seguinte:")
    for erro in erros:
        print(erro)


