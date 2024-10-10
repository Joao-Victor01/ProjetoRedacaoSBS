Sistema de Correção de Redações para a Competência 1 do ENEM

Este projeto desenvolve um sistema automatizado de correção de redações, focado na Competência 1 do ENEM, que avalia o domínio da norma padrão da língua escrita. O modelo utiliza técnicas de Sistemas Baseados em Conhecimento (SBS) para identificar e corrigir erros ortográficos, gramaticais e de concordância em textos.

Funcionalidades
Correção Ortográfica: Utiliza a biblioteca SymSpell para verificar e sugerir correções para palavras digitadas incorretamente.


Correção Gramatical: Aplica a ferramenta LanguageTool para identificar erros gramaticais e sugerir melhorias.


Verificação de Concordância: Detecta e corrige erros de concordância através de um arquivo de referência que pode ser atualizado continuamente.


Modelo de Previsão: Utiliza um modelo de regressão linear para prever a nota da redação, com base nas características do texto.


Tecnologias Utilizadas

Python: Linguagem de programação para o desenvolvimento do sistema.

scikit-learn: Biblioteca para a implementação do modelo de regressão linear.

SymSpell: Biblioteca para correção ortográfica.

LanguageTool: Biblioteca para correção gramatical.

Estrutura do Projeto

corretor.py: Script principal para treinamento e avaliação do modelo.

processamento.py: Contém funções para aplicar regras de correção.

errosConcordancia.txt: Arquivo de exemplos de erros de concordância.

modelo_treinado.pkl: Arquivo com o modelo treinado.

Como Usar

Clone o repositório:


git clone https://github.com/seu_usuario/nome_do_repositorio.git

cd nome_do_repositorio

Instale as dependências:

Utilize o arquivo requirements.txt para instalar as bibliotecas necessárias:


pip install -r requirements.txt
Treine o modelo:


Execute o script corretor.py para carregar o dataset e treinar o modelo:



python corretor.py

Corrija uma redação:


Utilize o script corrigirRedacao.py para inserir o texto da redação que deseja corrigir:

python corrigirRedacao.py

Contribuições
Contribuições são bem-vindas! Se você deseja melhorar o sistema, sinta-se à vontade para entrar em contato.

Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

Este sistema é uma ferramenta útil para estudantes que desejam aprimorar suas habilidades de escrita e estar mais preparados para o ENEM. Com a capacidade de aprender e se adaptar a novos erros, o sistema se torna cada vez mais eficiente na correção de redações.
