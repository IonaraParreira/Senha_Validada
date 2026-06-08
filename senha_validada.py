import re

print("\n--- SISTEMA DE SEGURANÇA: CADASTRO DE CREDENCIAIS ---\n")

# 1. Recebe a senha do usuário
senha = input("A senha tem que ter (mínimo 6 caracteres, com número e caractere especial): ")

# 2. A nova Regex explicada por partes:
# (?=.*\d)      -> SENSOR 1: Obriga a ter pelo menos um NÚMERO
# (?=.*[@$!%*?&]) -> SENSOR 2: Obriga a ter pelo menos um CARACTERE ESPECIAL
# .{6,}         -> REGRA 3: Mantém a exigência de ter no mínimo 6 caracteres no total
padrao_seguro = r"^(?=.*\d)(?=.*[@$!%*?&]).{6,}$"

# 3. Faz a validação
if re.fullmatch(padrao_seguro, senha):
    print("\n 🟢 Senha validada com sucesso!")
    
    # 4. Mantém o mascaramento que você gostou
    senha_escondida = "*" * len(senha)
    print(f"Sua senha foi mascarada para segurança: {senha_escondida}")

else:
    print("\n 🔴 Senha fraca!")
    print("Atenção: A senha deve ter pelo menos 6 caracteres, conter no mínimo 1 número e 1 caractere especial (ex: @, $, !, %, *, ?, &).")