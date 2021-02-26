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
