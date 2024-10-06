# Abrindo o arquivo txt, armazenando o seu conteúdo em uma variável
with open('treinamento.txt', mode='r') as f:
    treinamento = f.read()
# Mostrando uma parte do conteúdo do arquivo
print(treinamento[:500])
# Mostrando quantos caracteres têm no arquivo
len(treinamento)
# Um texto de exemplo
texto_exemplo = 'Olá, tudo bem?'
# "Tokenizando" o texto de exemplo utilizando o método split()
tokens = texto_exemplo.split()
# Mostrando o resultado da "tokenização" do texto de exemplo utilizando o método split()
print(tokens)
# Mostrando o tamanho da lista de tokens criadas no exemplo
len(tokens)
# Importando a biblioteca nltk
import nltk
# Baixando o pacote punkt
nltk.download('punkt')
# "Tokenizando" o texto de exemplo utilizando a biblioteca nltk
palavras_separadas = nltk.tokenize.word_tokenize(texto_exemplo)
# Mostrando o resultado da "tokenização" do texto de exemplo utilizando a biblioteca nltk
print(palavras_separadas)
# Mostrando o tamanho da lista de tokens criadas no exemplo
len(palavras_separadas)
# Relembrando como funciona o método isalpha()
'/.'.isalpha()
# Relembrando como funciona o método isalpha()
'à'.isalpha()
# Função separa_palavras()
def separa_palavras(lista_tokens):
    # Criando uma lista vazia para armazenar as palavras separadas dos caracteres especiais
    lista_palavras = []
    # Iterando por toda a lista de tokens
    for token in lista_tokens:
        # Separando as palavras dos caracteres especiais
        if token.isalpha():
            # Armazenando somente as palavras
            lista_palavras.append(token)    
    # Retornando uma lista somente com as palavras
    return lista_palavras
# Chamando a função separa_palavras para testar
separa_palavras(palavras_separadas)
# Uma pequena amostra do resultado até aqui
print(lista_palavras[:5])
# Função normalizacao() 
def normalizacao(lista_palavras):    
    # Criando uma lista vazia para armazenar as palavras normalizadas
    lista_normalizada = []
    # Iterando por toda a lista de palavras
    for palavra in lista_palavras:
        # Armazenando as palavras normalizadas
        lista_normalizada.append(palavra.lower())    
    # Retornando uma lista com as palavras normalizadas
    return lista_normalizada
# Chamando a função normalizacao()
lista_normalizada = normalizacao(lista_palavras)
# Uma pequena amostra do resultado até aqui
print(lista_normalizada[:5])
# Relembrando como funciona o método set() do Python
set([1, 2, 3, 3, 3, 4, 5, 6, 6])
# Mostrando o total real de palavras existentes em nosso corpus
print(f'O número total de palavras que nosso corretor "sabe" de fato é {len(set(lista_normalizada))}')
# Criando um exemplo
palavra_exemplo = 'programaão'
# Relembrando como fatiar uma string em Python
(palavra_exemplo[:8], palavra_exemplo[8:])
# Exemplo do que queremos fazer
print(f'{palavra_exemplo[:8]} + "a letra faltante (ç)" + {palavra_exemplo[8:]}'
      f'\n\nResulta na palavra \n\n\t{palavra_exemplo[:8] + "ç" + palavra_exemplo[8:]}')
# Função insere_letras()
# Recebe uma lista de tuplas (esquerdo, direito) que corresponde aos lados 
    # esquerdo e direito da palavra fatiada em dois
def insere_letras(fatias):
    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []
    # Variável que armazena todas as letras do alfabeto e as vogais acentuadas
        # É daqui que nosso corretor pegará a letra faltante
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:
        # Iterando por toda letra das variável letras
        for letra in letras:
            # Acrescentando todas as possibilidades de palavras possíveis
            novas_palavras.append(esquerdo + letra + direito)    
    # Retornando uma lista de possíveis palavras
    return novas_palavras
# Mostrando uma parte da lista que a função insere_letras() retorna como exemplo
insere_letras([('programa', 'ão')])[:5]
# Função gerador_palavras()
def gerador_palavras(palavra):
    # Criando uma lista vazia para armazenar as duas fatias de cada palavra
    fatias = []
    # Iterando por cada letra de cada palavra
    for i in range(len(palavra) + 1):
        # Armazenando as duas fatias em uma tupla e essa tupla em uma lista
        fatias.append((palavra[:i], palavra[i:]))
    # Chamando a função insere_letras() com a lista de tuplas das fatias 
        # recém-criadas e armazenando o retorno dessa função em uma variável
    palavras_geradas = insere_letras(fatias)
    # Retornando a lista de possíveis palavras. A palavra correta estará aí no meio
    return palavras_geradas
# Chamando a função gerador_palavras() com a pallavra_exemplo como parãmetro
    # e armazenando a lista que ela retorna em uma variável
palavras_geradas = gerador_palavras(palavra_exemplo)
# Mostrando, como exemplo, uma parte da lista que a função gerador_palavras() retorna
print(palavras_geradas[:5])
# Laço para mostrar que a palavra correta está aí dentro desta lista
for palavra in palavras_geradas:
    # Selecionando a palavra correta
    if palavra == 'programação':
        # Mostrando que a palavra correta está dentro dessa lista
        print(f'A palavra correta é "{palavra}" e ela está dentro da lista palavras_geradas')
# Mostrando a quantidade de palavras que a função gerador_palavras() 
    # retornou a partir da palavra_exemplo
print(f'Foram geradas {len(palavras_geradas)} palavras')
# Chamando a função FreqDist() com a lista_normalizada como parâmetro e 
    # armazenando o seu retorno em uma variável
frequencia = nltk.FreqDist(lista_normalizada)
# Calculando o total de palavras e armazenando esse número em uma variável
total_palavras = len(lista_normalizada)
# Mostrando as 10 palavras mais comuns da nossa lista_normalizada
frequencia.most_common(10)
# Função probabilidade()
def probabilidade(palavra_gerada):
    # Retorna a probabilidade de determinada palavra aparecer no nosso corpus
    return frequencia[palavra_gerada] / total_palavras
# Função corretor()
# Recebe como parâmetro a palavra errada (faltando uma letra) e retorna ela corrigida
def corretor(palavra_errada):
    # Chama a função gerador_palavras() usando como parâmetro a palavra 
        # de forma incoreta (digitada com uma letra faltando)
    palavras_geradas = gerador_palavras(palavra_errada)
    # Selecionando a palavra com maior probabilidade de aparecer em nosso corpus
    # Essa será a palavra correta
    palavra_correta = max(palavras_geradas, key=probabilidade)
    # Retornando a palavra corrigida
    return palavra_correta
# Recriando um exemplo, só pra não esquecer. Note que a palavra_exemplo está 
    # digitada incorretamente (faltando uma letra)
palavra_exemplo = 'programaão'
# Testando o nosso corrtor até aqui
corretor(palavra_exemplo)
# Mais testes. Agora com a palavra "lógica"
teste = 'lgica'
print(f'Você quis dizer: {corretor(teste)}')
# Função cria_dados_teste()
# Recebe o nome de um arquivo com uma série de palavras digitadas correta e 
    # incorretamente para podermos avaliar o nosso corretor
def cria_dados_teste(nome_arquivo):
    # Criando um lista vazia para armazenar as palavras de teste
    lista_palavras_teste = []
    # Abre o arquivo em mode de leitura
    f = open(nome_arquivo, 'r')
    # Iterando em toda linha do conteúdo do arquivo de teste
    for linha in f:
        # Separando as palavras digitadas correta e incorretamente avaliarmos
        correta, errada = linha.split()
        # Armazenando em uma lista as tuplas formadas pelas palavras 
            # digitadas correta e incorretamente
        lista_palavras_teste.append((correta, errada))    
    # Fechando o arquivo
    f.close()
    # Retornando a lista com as tuplas de palavras
        # digitadas coreta e incorretamante
    return lista_palavras_teste
# Chamando a função cria_dados_teste() com o nome do arquivo que contém as
    # palavras de teste
lista_teste = cria_dados_teste('palavras.txt')
# Função avaliador()
# Recebe uma lista com as tuplas de palavras de teste para poder
    # avaliar o nosso corretor
def avaliador(testes):
    # Calculando o número de palavras da lista de teste
    numero_palavras = len(testes)
    # Setando um contador
    acertou = 0
    # Iterando por cada tupla dentro da lista de teste
    for correta, errada in testes:
        # Chamando a função corretor() passando cada palavra
            # digitada incorretamente
        palavra_corrigida = corretor(errada)
        # Conferindo cada palavra para ver se ele conseguiu corrigir
        if palavra_corrigida == correta:
            # Incrementando o contador
            acertou += 1    
    # Calculando a taxa de acerto do nosso corretor
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)
    # Mostrando a taxa de acerto doe nosso corretor
    print(f'{taxa_acerto}% de {numero_palavras} palavras')
# Chamando a função avaliador()
avaliador(lista_teste)
# Função deletando_caracter()
# Recebe as fatias
def deletando_caracter(fatias):
    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []
    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:
        # Acrescentando todas as possibilidades de palavras possíveis
        novas_palavras.append(esquerdo + direito[1:])    
    # Retornando uma lista de possíveis palavras
    return novas_palavras
# Criando um exemplo para testarmos a nova função
exemplo = [('progr', 'samação')]
# Chamando a função deletando_caracter() passando como parâmetro um exemplo
deletando_caracter(exemplo)
# Refatorando a função gerador_palavras()
def gerador_palavras(palavra):
    # Criando uma lista vazia para armazenar as duas fatias de cada palavra
    fatias = []
    # Iterando por cada letra de cada palavra
    for i in range(len(palavra) + 1):
        # Armazenando as duas fatias em uma tupla e essa tupla em uma lista
        fatias.append((palavra[:i], palavra[i:]))
    # Chamando a função insere_letras() com a lista de tuplas das fatias 
        # recém-criadas e armazenando o retorno dessa função em uma variável
    palavras_geradas = insere_letras(fatias)
    # Acrescentando mais uma função
    # É aqui que a refatoração de fato ocorre
    palavras_geradas += deletando_caracter(fatias)
    # Retornando a lista de possíveis palavras. A palavra correta estará aí no meio
    return palavras_geradas
# Criando uma palavra de exemplo para testar a nova função gerador_palavras
palavra_exemplo = 'progrsamação'
# Chamando a função gerador_palavras() com a palavra_exemplo como parãmetro
    # e armazenando a lista que ela retorna em uma variável
palavras_geradas = gerador_palavras(palavra_exemplo)
# Mostrando, como exemplo, uma parte da lista que a função gerador_palavras() retorna
print(palavras_geradas[:5])
# Laço para mostrar que a palavra correta está aí dentro desta lista
for palavra in palavras_geradas:
    # Selecionando a palavra correta
    if palavra == 'programação':
        # Mostrando que a palavra correta está dentro dessa lista
        print(f'A palavra correta é "{palavra}" e ela está dentro da lista palavras_geradas')
# Mostrando a quantidade de palavras que a função gerador_palavras() 
    # retornou a partir da palavra_exemplo
print(f'Foram geradas {len(palavras_geradas)} palavras')
# Chamando a função que avalia o nosso corretor
avaliador(lista_teste)
# Função trocando_caracter()
# Recebe uma lista de tuplas (esquerdo, direito) que corresponde aos lados 
    # esquerdo e direito da palavra fatiada em dois
def troca_caracter(fatias):
    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []
    # Variável que armazena todas as letras do alfabeto e as vogais acentuadas
        # É daqui que nosso corretor pegará a letra faltante
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:
        # Iterando por toda letra das variável letras
        for letra in letras:
            # Acrescentando todas as possibilidades de palavras possíveis
            novas_palavras.append(esquerdo + letra + direito[1:])    
    # Retornando uma lista de possíveis palavras
    return novas_palavras
# Mostrando uma parte da lista que a função trocando_caracter() retorna como exemplo
troca_caracter([('prog', 'tamação')])[:5]
# Refatorando mais uma vez a função gerador_palavras()
def gerador_palavras(palavra):
    # Criando uma lista vazia para armazenar as duas fatias de cada palavra
    fatias = []
    # Iterando por cada letra de cada palavra
    for i in range(len(palavra) + 1):
        # Armazenando as duas fatias em uma tupla e essa tupla em uma lista
        fatias.append((palavra[:i], palavra[i:]))
    # Chamando a função insere_letras() com a lista de tuplas das fatias 
        # recém-criadas e armazenando o retorno dessa função em uma variável
    palavras_geradas = insere_letras(fatias)
    # Primeira refatoração
    palavras_geradas += deletando_caracter(fatias)
    # Acrescentando outra função
    # É aqui que a segunda refatoração de fato ocorre
    palavras_geradas += troca_caracter(fatias)
    # Retornando a lista de possíveis palavras. A palavra correta estará aí no meio
    return palavras_geradas
# Criando uma palavra de exemplo para testar a nova função gerador_palavras
palavra_exemplo = 'progtamação'
# Chamando a função gerador_palavras() com a palavra_exemplo como parãmetro
    # e armazenando a lista que ela retorna em uma variável
palavras_geradas = gerador_palavras(palavra_exemplo)
# Mostrando, como exemplo, uma parte da lista que a função gerador_palavras() retorna
print(palavras_geradas[:5])
# Laço para mostrar que a palavra correta está aí dentro desta lista
for palavra in palavras_geradas:
    # Selecionando a palavra correta
    if palavra == 'programação':
        # Mostrando que a palavra correta está dentro dessa lista
        print(f'A palavra correta é "{palavra}" e ela está dentro da lista palavras_geradas')
########################### Função insere_letras() ############################

# Recebe uma lista de tuplas (esquerdo, direito) que corresponde aos lados 
    # esquerdo e direito da palavra fatiada em dois
def insere_letras(fatias):

    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []

    # Variável que armazena todas as letras do alfabeto e as vogais acentuadas
        # É daqui que nosso corretor pegará a letra faltante
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'

    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:

        # Iterando por toda letra das variável letras
        for letra in letras:

            # Acrescentando todas as possibilidades de palavras possíveis
            novas_palavras.append(esquerdo + letra + direito)
    
    # Retornando uma lista de possíveis palavras
    return novas_palavras

######################## Função deletando_caracter() ##########################

# Função deletando_caracter()
# Recebe as fatias
def deletando_caracter(fatias):

    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []

    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:

        # Acrescentando todas as possibilidades de palavras possíveis
        novas_palavras.append(esquerdo + direito[1:])
    
    # Retornando uma lista de possíveis palavras
    return novas_palavras

######################## Função trocando_caracter() ###########################

# Função trocando_caracter()
# Recebe uma lista de tuplas (esquerdo, direito) que corresponde aos lados 
    # esquerdo e direito da palavra fatiada em dois
def troca_caracter(fatias):

    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []

    # Variável que armazena todas as letras do alfabeto e as vogais acentuadas
        # É daqui que nosso corretor pegará a letra faltante
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'

    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:

        # Iterando por toda letra das variável letras
        for letra in letras:

            # Acrescentando todas as possibilidades de palavras possíveis
            novas_palavras.append(esquerdo + letra + direito[1:])
    
    # Retornando uma lista de possíveis palavras
    return novas_palavras

####################### Função invertendo_caracter() ##########################

# Função invertendo_caracter()
# Recebe as fatias
def invertendo_caracter(fatias):

    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []

    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:
        
        # Selecionando apenas as fatias da direita que têm mais de uma letra, 
            # pois, se não, não há o que inverter
        if len(direito) > 1:
            
            # Acrescentando todas as possibilidades de palavras possíveis
            novas_palavras.append(esquerdo + direito[1] + direito[0] + direito[2:])
    
    # Retornando uma lista de possíveis palavras
    return novas_palavras

######################### Função gerador_palavras() ###########################

# Refatorando outra vez a função gerador_palavras()
def gerador_palavras(palavra):

    # Criando uma lista vazia para armazenar as duas fatias de cada palavra
    fatias = []

    # Iterando por cada letra de cada palavra
    for i in range(len(palavra) + 1):

        # Armazenando as duas fatias em uma tupla e essa tupla em uma lista
        fatias.append((palavra[:i], palavra[i:]))

    # Chamando a função insere_letras() com a lista de tuplas das fatias 
        # recém-criadas e armazenando o retorno dessa função em uma variável
    palavras_geradas = insere_letras(fatias)

    # Primeira refatoração
    palavras_geradas += deletando_caracter(fatias)

    # Segunda refatoração de fato ocorre
    palavras_geradas += troca_caracter(fatias)

    # Acrescentando outra função
    # É aqui que a terceira refatoração de fato ocorre
    palavras_geradas += invertendo_caracter(fatias)

    # Retornando a lista de possíveis palavras. A palavra correta estará aí no meio
    return palavras_geradas
################################# AVALIANDO ###################################

# Criando uma palavra de exemplo para testar a nova função gerador_palavras
# Note o novvo erro de digitação
palavra_exemplo = 'prorgamação'

# Chamando a função gerador_palavras() com a palavra_exemplo como parãmetro
    # e armazenando a lista que ela retorna em uma variável
palavras_geradas = gerador_palavras(palavra_exemplo)

# Mostrando, como exemplo, uma parte da lista que a função gerador_palavras() retorna
print(palavras_geradas[:5])
# Laço para mostrar que a palavra correta está aí dentro desta lista
for palavra in palavras_geradas:

    # Selecionando a palavra correta
    if palavra == 'programação':

        # Mostrando que a palavra correta está dentro dessa lista
        print(f'A palavra correta é "{palavra}" e ela está dentro da lista palavras_geradas')
        # Chamando a função que avalia o nosso corretor
avaliador(lista_teste)
# Função avaliador()
# Recebe uma lista com as tuplas de palavras de teste para poder
    # avaliar o nosso corretor
def avaliador(testes, vocabulario):

    # Calculando o número de palavras da lista de teste
    numero_palavras = len(testes)

    # Setando os contadores
    acertou = desconhecidas = 0

    # Iterando por cada tupla dentro da lista de teste
    for correta, errada in testes:

        # Chamando a função corretor() passando cada palavra
            # digitada incorretamente
        palavra_corrigida = corretor(errada)

        # Incrementando o contador das palavras desconhecidas
        desconhecidas += (correta not in vocabulario)
        
        # Conferindo cada palavra para ver se ele conseguiu corrigir
        if palavra_corrigida == correta:

            # Incrementando o contador das palavras corretas
            acertou += 1
    
    # Calculando a taxa de acerto do nosso corretor
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)

    # Calculando a taxa de erro referente às palavras desconhecidas
    taxa_desconhecidas = round(desconhecidas * 100 / numero_palavras, 2)

    # Mostrando a taxa de acerto doe nosso corretor
    print(f'{taxa_acerto}% de {numero_palavras} das palavras conhecidas\n'
          f'e {taxa_desconhecidas}% das palavras desconhecidas')

# Calculando as palavras conecidas
vocabulario = set(lista_normalizada)

# Chamando a função avaliador()
avaliador(lista_teste, vocabulario),palavra_exemplo = 'prorrgramação'
corretor(palavra_exemplo)
# Função gerador_inception()
def gerador_inception(palavras_geradas):

    # Criando uma nova lista para armazenar as novas palavras
    novas_palavras = []

    # Iterando em cada palavra da lista recebida
    for palavra in palavras_geradas:

        # Chamando a função gerador_palavras() aqui dentro da nova função
            # Por isso o nome gerador_inception()
        novas_palavras += gerador_palavras(palavra)
    
    # Retornando as novas palavras
    return novas_palavras
# Calculando o número de palavras geradas ao chamar a função gerador_palavras()
    # dentro da função gerador_inception()
palavras_geradas = gerador_inception(gerador_palavras(palavra_exemplo))
print(f'A quantidade de possíveis palavras geradas é {len(palavras_geradas)}')
# Mostrando que a palavra correta está nesse monte de lixo

'programação' in palavras_geradas
# Função corretor_super_sayajin()
# Recebe como parâmetro a palavra errada e retorna ela corrigida
def corretor_super_sayajin(palavra_errada):

    # Chama a função gerador_palavras() usando como parâmetro a palavra 
        # escrita de forma incorreta
    palavras_geradas = gerador_palavras(palavra_errada)

    # Chamando a função gerador_inception() e armazenando o seu retorno
        # em uma variável
    palavras_inception = gerador_inception(palavras_geradas)

    # Juntando todas as palavras geradas
    todas_palavras = set(palavras_geradas + palavras_inception)

    # Criando uma lista para armazenar os possíveis candidatos a palavra 
    candidatos = [palavra_errada]

    # Iterando por todas as palavras geradas pelas duas funções
    for palavra in todas_palavras:

        # Verificando se a palavra já se encontra no vocabulário
        if palavra in vocabulario:

            # Adicionando a palvara a lista de candidatos
            candidatos.append(palavra)

    # Mostrando quantos e quais são os candidatos
    print(f'Temos {len(candidatos)} candidatos a palavra correta.\n'
          f'São eles {candidatos}')

    # Selecionando a palavra com maior probabilidade de aparecer em nosso corpus
        # Essa será a palavra correta
    palavra_correta = max(candidatos, key=probabilidade)

    # Retornando a palavra corrigida
    return palavra_correta
# Chamando a função antiga função corretor()
antes = corretor(palavra_exemplo)

# Mostrando o retorno da antiga função corretor()
print('Antiga função corretor()\n'
      '========================\n\n'
     f'Entrada ==> {palavra_exemplo}\n'
     f'Retorno ==> {antes}')
# Um print() para melhor visualizar os resultados
print('Com a novoa função corretor_super_sayajin():\n')

# Chamando a função nova função corretor_super_sayajin()
depois = corretor_super_sayajin(palavra_exemplo)

# Mostrando o retorno da nova função corretor_super_sayajin()
print('\nNova função nova função corretor_super_sayajin()\n'
      '==============================================\n\n'
     f'Entrada ==> {palavra_exemplo}\n'
     f'Retorno ==> {depois}')
# Função corretor_super_sayajin()
# Recebe como parâmetro a palavra errada e retorna ela corrigida
def corretor_super_sayajin(palavra_errada):

    # Chama a função gerador_palavras() usando como parâmetro a palavra 
        # escrita de forma incorreta
    palavras_geradas = gerador_palavras(palavra_errada)

    # Chamando a função gerador_inception() e armazenando o seu retorno
        # em uma variável
    palavras_inception = gerador_inception(palavras_geradas)

    # Juntando todas as palavras geradas
    todas_palavras = set(palavras_geradas + palavras_inception)

    # Criando uma lista para armazenar os possíveis candidatos a palavra 
    candidatos = [palavra_errada]

    # Iterando por todas as palavras geradas pelas duas funções
    for palavra in todas_palavras:

        # Verificando se a palavra já se encontra no vocabulário
        if palavra in vocabulario:

            # Adicionando a palvara a lista de candidatos
            candidatos.append(palavra)

    # Selecionando a palavra com maior probabilidade de aparecer em nosso corpus
        # Essa será a palavra correta
    palavra_correta = max(candidatos, key=probabilidade)

    # Retornando a palavra corrigida
    return palavra_correta
     

# Mostrando que a nova função corretor_super_sayajin() não imprime mais 
    # quantos e quias são os possíveis candidatos
corretor_super_sayajin(palavra_exemplo)
# Função avaliador()
# Recebe uma lista com as tuplas de palavras de teste para poder
    # avaliar o nosso corretor
def avaliador(testes, vocabulario):

    # Calculando o número de palavras da lista de teste
    numero_palavras = len(testes)

    # Setando os contadores
    acertou = desconhecidas = 0

    # Iterando por cada tupla dentro da lista de teste
    for correta, errada in testes:

        # Chamando a função corretor() passando cada palavra
            # digitada incorretamente
        palavra_corrigida = corretor_super_sayajin(errada)

        # Incrementando o contador das palavras desconhecidas
        desconhecidas += (correta not in vocabulario)
        
        # Conferindo cada palavra para ver se ele conseguiu corrigir
        if palavra_corrigida == correta:

            # Incrementando o contador das palavras corretas
            acertou += 1
    
    # Calculando a taxa de acerto do nosso corretor
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)

    # Calculando a taxa de erro referente às palavras desconhecidas
    taxa_desconhecidas = round(desconhecidas * 100 / numero_palavras, 2)

    # Mostrando a taxa de acerto doe nosso corretor
    print(f'{taxa_acerto}% de {numero_palavras} das palavras conhecidas\n'
          f'e {taxa_desconhecidas}% das palavras desconhecidas')

# Calculando as palavras conecidas
vocabulario = set(lista_normalizada)

# Chamando a função avaliador()
avaliador(lista_teste, vocabulario)
# Função avaliador()
# Recebe uma lista com as tuplas de palavras de teste para poder
    # avaliar o nosso corretor
def avaliador(testes, vocabulario):

    # Calculando o número de palavras da lista de teste
    numero_palavras = len(testes)

    # Setando os contadores
    acertou = desconhecidas = 0

    # Iterando por cada tupla dentro da lista de teste
    for correta, errada in testes:

        # Chamando a função corretor() passando cada palavra
            # digitada incorretamente
        palavra_corrigida = corretor_super_sayajin(errada)

        # Incrementando o contador das palavras desconhecidas
        desconhecidas += (correta not in vocabulario)
        
        # Conferindo cada palavra para ver se ele conseguiu corrigir
        if palavra_corrigida == correta:

            # Incrementando o contador das palavras corretas
            acertou += 1

        #
        else:
            print(f"{errada} - {corretor(errada)} - {palavra_corrigida}")
    
    # Calculando a taxa de acerto do nosso corretor
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)

    # Calculando a taxa de erro referente às palavras desconhecidas
    taxa_desconhecidas = round(desconhecidas * 100 / numero_palavras, 2)

    # Mostrando a taxa de acerto doe nosso corretor
    print(f'\n\n{taxa_acerto}% de {numero_palavras} das palavras conhecidas\n'
          f'e {taxa_desconhecidas}% das palavras desconhecidas')

# Calculando as palavras conecidas
vocabulario = set(lista_normalizada)

# Chamando a função avaliador()
avaliador(lista_teste, vocabulario)
########################### Função insere_letras() ############################

# Recebe uma lista de tuplas (esquerdo, direito) que corresponde aos lados 
    # esquerdo e direito da palavra fatiada em dois
def insere_letras(fatias):

    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []

    # Variável que armazena todas as letras do alfabeto e as vogais acentuadas
        # É daqui que nosso corretor pegará a letra faltante
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'

    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:

        # Iterando por toda letra das variável letras
        for letra in letras:

            # Acrescentando todas as possibilidades de palavras possíveis
            novas_palavras.append(esquerdo + letra + direito)
    
    # Retornando uma lista de possíveis palavras
    return novas_palavras

######################## Função deletando_caracter() ##########################

# Função deletando_caracter()
# Recebe as fatias
def deletando_caracter(fatias):

    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []

    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:

        # Acrescentando todas as possibilidades de palavras possíveis
        novas_palavras.append(esquerdo + direito[1:])
    
    # Retornando uma lista de possíveis palavras
    return novas_palavras

######################## Função trocando_caracter() ###########################

# Função trocando_caracter()
# Recebe uma lista de tuplas (esquerdo, direito) que corresponde aos lados 
    # esquerdo e direito da palavra fatiada em dois
def troca_caracter(fatias):

    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []

    # Variável que armazena todas as letras do alfabeto e as vogais acentuadas
        # É daqui que nosso corretor pegará a letra faltante
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'

    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:

        # Iterando por toda letra das variável letras
        for letra in letras:

            # Acrescentando todas as possibilidades de palavras possíveis
            novas_palavras.append(esquerdo + letra + direito[1:])
    
    # Retornando uma lista de possíveis palavras
    return novas_palavras

####################### Função invertendo_caracter() ##########################

# Função invertendo_caracter()
# Recebe as fatias
def invertendo_caracter(fatias):

    # Criando uma lista vazia para armazenar as palavras corrigidas
    novas_palavras = []

    # Iterando por todas as tuplas da lista recebida
    for esquerdo, direito in fatias:
        
        # Selecionando apenas as fatias da direita que têm mais de uma letra, 
            # pois, se não, não há o que inverter
        if len(direito) > 1:
            
            # Acrescentando todas as possibilidades de palavras possíveis
            novas_palavras.append(esquerdo + direito[1] + direito[0] + direito[2:])
    
    # Retornando uma lista de possíveis palavras
    return novas_palavras

######################### Função gerador_palavras() ###########################

# Refatorando outra vez a função gerador_palavras()
def gerador_palavras(palavra):

    # Criando uma lista vazia para armazenar as duas fatias de cada palavra
    fatias = []

    # Iterando por cada letra de cada palavra
    for i in range(len(palavra) + 1):

        # Armazenando as duas fatias em uma tupla e essa tupla em uma lista
        fatias.append((palavra[:i], palavra[i:]))

    # Chamando a função insere_letras() com a lista de tuplas das fatias 
        # recém-criadas e armazenando o retorno dessa função em uma variável
    palavras_geradas = insere_letras(fatias)

    # Primeira refatoração
    palavras_geradas += deletando_caracter(fatias)

    # Segunda refatoração de fato ocorre
    palavras_geradas += troca_caracter(fatias)

    # Acrescentando outra função
    # É aqui que a terceira refatoração de fato ocorre
    palavras_geradas += invertendo_caracter(fatias)

    # Retornando a lista de possíveis palavras. A palavra correta estará aí no meio
    return palavras_geradas

############################# Função avaliador() ###############################

# Função avaliador()
# Recebe uma lista com as tuplas de palavras de teste para poder
    # avaliar o nosso corretor
def avaliador(testes, vocabulario):

    # Calculando o número de palavras da lista de teste
    numero_palavras = len(testes)

    # Setando os contadores
    acertou = desconhecidas = 0

    # Iterando por cada tupla dentro da lista de teste
    for correta, errada in testes:

        # Chamando a função corretor() passando cada palavra
            # digitada incorretamente
        palavra_corrigida = corretor(errada)

        # Incrementando o contador das palavras desconhecidas
        desconhecidas += (correta not in vocabulario)
        
        # Conferindo cada palavra para ver se ele conseguiu corrigir
        if palavra_corrigida == correta:

            # Incrementando o contador das palavras corretas
            acertou += 1
    
    # Calculando a taxa de acerto do nosso corretor
    taxa_acerto = round(acertou * 100 / numero_palavras, 2)

    # Calculando a taxa de erro referente às palavras desconhecidas
    taxa_desconhecidas = round(desconhecidas * 100 / numero_palavras, 2)

    # Mostrando a taxa de acerto doe nosso corretor
    print(f'{taxa_acerto}% de {numero_palavras} das palavras conhecidas\n'
          f'e {taxa_desconhecidas}% das palavras desconhecidas')

# Calculando as palavras conecidas
vocabulario = set(lista_normalizada)

# Chamando a função avaliador()
avaliador(lista_teste, vocabulario)