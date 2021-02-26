# Cobertura de testes

Para os testes de cobertura, é usado o coverage, ele não é nativo do Python e pode ser instalado com o comando abaixo:

```bash
pip install coverage
```

OBS: ```Ao fazer a instalação do requirements.txt o coverage será instalado.```

Como o framework de testes de unidade usado é o unittest, o comando que será usado é:

```bash
coverage run -m unittest test_core
```

Onde a saída deverá ser algo como a mostrada abaixo:

```bash
Name                 Stmts   Miss  Cover
----------------------------------------
app.py                   9      1    89%
resources/hello.py       4      0   100%
resources/login.py      10      1    90%
----------------------------------------
TOTAL                   23      2    91%
```
