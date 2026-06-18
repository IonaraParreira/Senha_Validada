import re

print("\n--- SISTEMA DE SEGURANÇA: CADASTRO DE CREDENCIAIS ---\n")

# 1. Recebe a senha do usuário
senha = input("A senha tem que ter (mínimo 8 caracteres, incluindo: maiúscula,minúscula, número e caractere especial): ")

# 2. A nova Regex explicada por partes:
# ^             -> Início da string
# (?=.*\d)      -> SENSOR 1: Obriga a ter pelo menos um NÚMERO
# (?=.*[@$!%*?&#]) -> SENSOR 2: Obriga a ter pelo menos um CARACTERE ESPECIAL
# (?=.*[A-Z])   -> SENSOR 3: Obriga a ter pelo menos uma letra MAIÚSCULA
# (?=.*[a-z])   -> SENSOR 4: Obriga a ter pelo menos uma letra MINÚSCULA
# .{8,}         -> REGRA 5: Mantém a exigência de ter no mínimo 8 caracteres no total
# $             -> Fim da string
padrao_seguro = r"^(?=.*\d)(?=.*[@$!%*?&#])(?=.*[A-Z])(?=.*[a-z]).{8,}$"

# 3. Faz a validação
if re.fullmatch(padrao_seguro, senha):
    print("\n 🟢 Senha validada com sucesso!")
    
    # 4. Mantém o mascaramento 
    senha_escondida = "*" * len(senha)
    print(f"Sua senha foi mascarada para segurança: {senha_escondida}")

else:
    print("\n 🔴 Senha fraca!")
    print("Atenção: A senha deve ter pelo menos 8 caracteres, conter no mínimo 1 número e 1 caractere especial(ex: @, $, !, %, *, ?, &),1 letra maiúscula e 1 letra minúscula.")
