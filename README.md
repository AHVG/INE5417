## Sobre

O jogo desenvolvido é o Ultimate Tic Tac Toe. Para saber como funciona, é possível ver o pdf "Especificação de requisitos Ultimate Tic Tac Toe.pdf", que está na pasta "/doc", onde consta tudo referente a casos de uso, o jogo em si e mais. Também na pasta "/doc" temos o "UltimateTicTacToe_UML.vpp". Este arquivo possui diagramas de estado, de sequência, de atividade, de algoritmo, de visão geral e de casos de uso referentes ao jogo implementado. Para abrí-lo use Visual Paradigm.

## Como executar o projeto <a id='como-executar-o-projeto'></a>

### 1º Etapa

Criar ambiente virtual chamado venv 

`python3 -m venv venv`

Para saber com mais detalhes como baixar a biblioteca venv e criar o ambiente, veja a [documentação](https://docs.python.org/pt-br/3/library/venv.html)

### 2º Etapa

Depois de criar, agora é preciso ativá-lo

`source venv/bin/activate`

### 3º Etapa

Após configurado corretamente o ambiente virtual, agora é necessário baixar as dependências

`pip3 install -r requirements.txt`

### 4º Etapa

Com as dependências, falta iniciar o jogo, estando em "src":

`python3 main.py`

## Como executar os testes

Antes de prosseguir, é interessante observar que o uso do Tkinter limitou muito a produção de testes, uma vez que ele não tem suporte a threads/processos. Esta limitação, dificultou em muito a simulação de dois players, por isso os testes de flow não ficaram dos melhores.

### 1º Etapa

Ativar o ambiente virtual assim como foi ativado na seção de [Como executar o projeto](#como-executar-o-projeto) 

### 2º Etapa

Na pasta "src", execute o seguinte código para rodar todos os testes: de flow e unitários.

`python3 -m pytest ./tests/`

Se quiser rodar individualmente os testes de flow ou unitário, digite o seguinte comando:

`python3 -m pytest ./tests/unit/test_models/test_board.py`

Note, no exemplo, executará o teste do board, mas, se, por exemplo, queremos rodar o do RoundManager, digitariamos o seguinte comando:

`python3 -m pytest ./tests/unit/test_controllers/test_round_manager.py`

Para o teste de flow é análogo...

### Observações

- As versões do python utilizadas e testadas foram 3.10 e 3.11 (OBS: Não quer dizer que em outras versões não funcione, mas apenas que seu funcionamento foi verificado para essas versões)
- A versão do pip usado foi 22.0.2
- O código foi testado sobretudo em ambiente linux, especificamente no Ubuntu 22.04.4 LTS. Assim, pode haver problemas quando rodado em ambiente diferente, principalmente na etapas um, dois e três do [Como executar o projeto](#como-executar-o-projeto)