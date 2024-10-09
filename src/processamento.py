import re
from symspellpy import SymSpell, Verbosity
import unicodedata
import language_tool_python

# Inicializar LanguageTool para português
tool = language_tool_python.LanguageTool('pt-BR')

# Inicializar SymSpell
symspell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Carregar o dicionário
dicionario_path = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\dicionarios\dicionario_combinado.txt"
symspell.load_dictionary(dicionario_path, term_index=0, count_index=1)

# Função para normalizar palavras (remover acentuação)
def remover_acentuacao(palavra):
    nfkd_form = unicodedata.normalize('NFKD', palavra)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

# Função para aplicar correções ortográficas usando SymSpell
def aplicar_regras_conhecimento(texto):
    erros_ortograficos = []

    palavras = texto.split()
    print(f"Total de palavras a processar: {len(palavras)}")
    for palavra in palavras:
        palavra_normalizada = remover_acentuacao(palavra.strip('.,!?"\'').lower())
        print(f"Processando palavra: {palavra_normalizada}")
        sugestões = symspell.lookup(palavra_normalizada, Verbosity.CLOSEST, 2)
        if sugestões:
            palavra_correta = sugestões[0].term
            if palavra_correta != palavra_normalizada:
                print(f"Palavra incorreta: {palavra_normalizada} -> Correção sugerida: {palavra_correta}")
                erros_ortograficos.append((palavra, palavra_correta))

    return erros_ortograficos

# Função para aplicar correções gramaticais com LanguageTool
def aplicar_languagetool(texto):
    print("Aplicando LanguageTool para correção gramatical...")
    sentencas = texto.split('. ')
    erros_gramaticais = []

    for sentenca in sentencas:
        matches = tool.check(sentenca)
        for match in matches:
            erro_original = match.context
            sugerido = match.replacements[0] if match.replacements else "Nenhuma sugestão disponível"
            mensagem = f"Erro detectado: \"{erro_original}\" \n" \
                       f"Sugestão: \"{sugerido}\" \n" \
                       f"Descrição: {match.message}\n"
            print(mensagem)
            erros_gramaticais.append(mensagem)

    return erros_gramaticais