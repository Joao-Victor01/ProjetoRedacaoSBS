1. Módulos necessários para rodar o script redacoes.py:
Para rodar o script redacoes.py com o carregamento das redações a partir do pacote uol_redacoes_xml, os seguintes módulos foram necessários:

-> uol_redacoes_xml: Para carregar as redações.
-> bs4 (BeautifulSoup): Utilizado pelo pacote uol_redacoes_xml para parsing de HTML.
-> requests: Para fazer requisições HTTP no pacote.
-> nltk: Para tokenização e outras funcionalidades de Processamento de Linguagem Natural (PLN) no pacote.
-> scikit-learn (sklearn): Necessário para manipulação de dados e possíveis implementações de aprendizado de máquina dentro do pacote.
-> matplotlib: Para visualização e gráficos, possivelmente utilizado em algum ponto pelo pacote uol_redacoes_xml.
-> lxml: Um parser XML adicional.
-> threadpoolctl, joblib: Dependências do Scikit-learn para controle de recursos e paralelismo.
-> tqdm: Para barras de progresso.
-> numpy e scipy: Bibliotecas usadas como base para manipulação numérica e estatística (necessárias para o scikit-learn).

2. Tags do XML que contêm os atributos sobre a redação:
Com base nas informações extraídas do XML, o conteúdo das redações e suas notas por competência foram identificados nas seguintes tags:

Texto da Redação:
Tag: <original>
Contém o texto original da redação, ou seja, o conteúdo textual que o aluno escreveu.


Notas por Competência:
Tag: <criteria>
Dentro dessa tag, estão as notas atribuídas às competências avaliadas. Cada critério é identificado por uma tag <criterion>, e cada uma delas contém:
-> Nome da competência: A tag <name> dentro de <criterion> descreve qual competência está sendo avaliada.
-> Nota da competência: A tag <score> dentro de <criterion> contém a nota atribuída a essa competência.