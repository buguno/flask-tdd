# Teste de unidade

Para o teste de unidade é usado o unittest, que é um framework que foi desenvolvido baseado no JUnit e já é nativo da linguagem Python.

## Test case

Rodando o comando a seguir, é possível fazer um test case, que é uma unidade individual de teste.

```bash
python -m unittest test_core.FlaskTestLogin.test_login
```

Onde a saída deverá ser algo como será mostrado abaixo:

```bash
.
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
```

## Test suite

Ou se preferir, podemos fazer um teste de tipo test suite, onde uma coleção de caso de teste.

```bash
python -m unittest test_core.FlaskTestCase
```

Onde a saída deverá ser algo como será mostrado abaixo:

```bash
..
----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK
```
