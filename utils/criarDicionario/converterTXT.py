import pdfplumber
import re

# Caminho do arquivo PDF
caminho_pdf = r"C:/Users/joao-/Downloads/dicionario.pdf"
caminho_saida = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\utils\criarDicionario\dicionario_limpo.txt"

# Conjunto para armazenar palavras únicas
palavras_unicas = set()

# Extrair texto do PDF
with pdfplumber.open(caminho_pdf) as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        if texto:
            # Dividir o texto em linhas
            linhas = texto.split('\n')
            for linha in linhas:
                # Usar regex para extrair a palavra (antes do primeiro espaço ou traço)
                palavra = re.match(r'^\s*(\S+)', linha)
                if palavra:
                    palavras_unicas.add(palavra.group(1))  # Adiciona a palavra ao conjunto

# Salvar as palavras únicas em um novo arquivo
with open(caminho_saida, 'w', encoding='utf-8') as file:
    for palavra in sorted(palavras_unicas):
        file.write(f"{palavra}\n")

print(f"Palavras limpas foram salvas em: {caminho_saida}")
