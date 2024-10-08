def process_bib_file(file_path):
    words = set()  # Usar um set para evitar duplicatas
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            if word:  # Verifica se a linha não está em branco
                words.add(word)
    return words

def merge_bib_files(files):
    combined_words = set()
    for file in files:
        combined_words.update(process_bib_file(file))
    
    return combined_words

def save_to_symspell_format(output_file, words):
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(words):  # Ordenar as palavras antes de salvar
            f.write(f"{word} 1\n")  # Usar "1" como frequência genérica

# Arquivos .bib
bib_files = [
    r'C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\dicionarios\bibFiles\pt-br\conjugações.bib',
    r'C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\dicionarios\bibFiles\pt-br\dicio.bib',
    r'C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\dicionarios\bibFiles\pt-br\palavras.bib',
    r'C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\dicionarios\bibFiles\pt-br\verbos.bib'
]

# Combinar arquivos e salvar
combined_words = merge_bib_files(bib_files)
output_file = r'C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\dicionarios\dicionario4.txt'
save_to_symspell_format(output_file, combined_words)

print(f"Dicionário combinado salvo em {output_file}")
