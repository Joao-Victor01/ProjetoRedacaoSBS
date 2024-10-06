def adaptar_para_symspell(caminho_entrada, caminho_saida):
    # Cria um conjunto para garantir palavras únicas
    palavras_unicas = set()
    
    # Lê o arquivo de entrada
    with open(caminho_entrada, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            # Remove espaços em branco e adicione a palavra ao conjunto
            palavra = linha.strip()
            if palavra:  # Ignora linhas vazias
                palavras_unicas.add(palavra.lower())  # Normaliza para minúsculas

    # Escreve as palavras únicas no formato para SymSpell
    with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
        for palavra in palavras_unicas:
            arquivo_saida.write(f"{palavra} 1\n")  # A contagem é 1 para cada palavra

# Definindo os caminhos conforme solicitado
caminho_entrada = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\dicionarios\palavras.txt"
caminho_saida = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\dicionarios\dicionario03.txt"

# Executando a função
adaptar_para_symspell(caminho_entrada, caminho_saida)
