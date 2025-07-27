# Sistema de Cadastro e Login com PyQt5

Este projeto é uma interface gráfica simples de **cadastro e login de usuários** construída com **Python e PyQt5**, com **salvamento de dados em arquivo JSON** para persistência local.

---

## Funcionalidades

- Tela de cadastro de usuário
- Tela de login com verificação de credenciais
- Validação de campos obrigatórios
- Armazenamento permanente dos dados no arquivo `usuarios.json`
- Interface estilizada via arquivo externo `estilo.qss`

---

## Tecnologias Utilizadas

- [Python 3.13.0](https://www.python.org)
- [PyQt5](https://pypi.org/project/PyQt5/)
- JSON para persistência de dados local

---

## Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/Everton-M/gui-interface.git
cd gui-interface
```

2. Instale a dependência:

pip install pyqt5

3. Execute o programa:

python main.py

## Estrutura do Projeto

## Estrutura do Projeto

```plaintext
.
├── main.py             # Arquivo principal da aplicação
├── tela_cadastro.py    # Interface e lógica da tela de cadastro
├── tela_login.py       # Interface e lógica da tela de login
├── dados.py            # Manipulação do arquivo JSON
├── usuarios.json       # Arquivo gerado com os usuários cadastrados
├── estilo.qss          # Estilo visual da interface (opcional)
└── README.md           # Este documento

```
