import re
import spacy
from symspellpy import SymSpell, Verbosity
import unicodedata  # Para normalizar a acentuação

# Carregar o modelo spaCy para português
nlp = spacy.load('pt_core_news_sm')

# Inicializar SymSpell
symspell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

# Carregar o dicionário
dicionario_path = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\dicionarios\dicionario_combinado.txt"
symspell.load_dictionary(dicionario_path, term_index=0, count_index=1)

# Função para normalizar palavras (remover acentuação)
def remover_acentuacao(palavra):
    nfkd_form = unicodedata.normalize('NFKD', palavra)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

# Função para aplicar regras de conhecimento (ortográficas e gramaticais)
def aplicar_regras_conhecimento(texto):
    erros_ortograficos = []
    erros_gramaticais = []

    # Corrigir palavras usando SymSpell
    palavras = texto.split()
    print(f"Total de palavras a processar: {len(palavras)}")
    for palavra in palavras:
        # Normalizando a palavra
        palavra_normalizada = remover_acentuacao(palavra.strip('.,!?"\'').lower())  # Remove pontuação, acentos e converte para minúsculas
        print(f"Processando palavra: {palavra_normalizada}")  # Verifique quais palavras estão sendo processadas
        sugestões = symspell.lookup(palavra_normalizada, Verbosity.CLOSEST, 2)
        if sugestões:
            palavra_correta = sugestões[0].term  # Pega a sugestão mais próxima
            if palavra_correta != palavra_normalizada:
                print(f"Palavra incorreta: {palavra_normalizada} -> Correção sugerida: {palavra_correta}")
                erros_ortograficos.append((palavra, palavra_correta))

    # Regras gramaticais (concordância simples)
    if re.search(r"\beu\b.*(vamos|fizemos)", texto):
        erros_gramaticais.append("Erro de concordância: 'eu' com 'vamos' ou 'fizemos'")

    # Aumentar a verificação gramatical com o spaCy
    doc = nlp(texto)
    for token in doc:
        if token.dep_ == "nsubj" and token.head.pos_ == "VERB":
            if token.tag_ != token.head.tag_:
                erros_gramaticais.append(f"Erro de concordância: {token.text} com {token.head.text}")

    return erros_ortograficos, erros_gramaticais

# Função para aplicar Processamento de Linguagem Natural (PLN)
def aplicar_pln(texto):
    print("Aplicando PLN com spaCy...")
    doc = nlp(texto)
    erros_gramaticais = []

    for token in doc:
        # Verificação de concordância simples
        print(f"Processando token: {token.text} ({token.dep_})")  # Acompanhe os tokens processados
        if token.dep_ == "nsubj" and token.head.pos_ == "VERB":
            if token.tag_ != token.head.tag_:
                erros_gramaticais.append(f"Erro de concordância: {token.text} com {token.head.text}")

    return erros_gramaticais
