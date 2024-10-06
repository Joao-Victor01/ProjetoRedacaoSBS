########################### Função corretor() ############################
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