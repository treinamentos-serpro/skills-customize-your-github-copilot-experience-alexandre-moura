# 📘 Atividade: Testes Automatizados com pytest

## 🎯 Objetivo

Aprenda a escrever e executar testes automatizados com `pytest` para verificar o comportamento de funções e classes, incluindo casos de erro, e a usar esses testes para encontrar e corrigir bugs.

## 📝 Tarefas

### 🛠️ Primeiros Testes com assert

#### Descrição
Instale o pytest com `pip install pytest` e copie o arquivo `starter-code.py` para `bank_account.py`. Em seguida, crie o arquivo `test_bank_account.py` no mesmo diretório, importe a classe `BankAccount` e a função `apply_interest` e escreva funções de teste que começam com `test_`. Execute os testes com `pytest -v`.

#### Requisitos
O programa concluído deve:

- Criar o arquivo `test_bank_account.py` com pelo menos 2 funções de teste para `deposit()`
- Verificar, com `assert`, que o saldo aumenta corretamente após um depósito
- Criar pelo menos 1 função de teste para `apply_interest()` verificando o resultado de um cálculo
- Executar `pytest -v` e obter todos os testes aprovados


### 🛠️ Testar Erros com pytest.raises

#### Descrição
Garanta que a conta rejeite operações inválidas. Use `pytest.raises()` para verificar se a exceção correta é lançada quando um valor inválido é passado ou quando o saldo não é suficiente.

#### Requisitos
O programa concluído deve:

- Testar que `deposit()` lança `ValueError` para valores zero ou negativos
- Testar que `withdraw()` lança `ValueError` para valores zero ou negativos
- Testar que `withdraw()` lança `ValueError` quando o valor do saque é maior que o saldo disponível
- Verificar a mensagem da exceção com o parâmetro `match` de `pytest.raises()` em pelo menos um teste

Exemplo de uso:

```python
with pytest.raises(ValueError, match="positivo"):
    account.deposit(-50)
```


### 🛠️ Parametrização e Fixtures

#### Descrição
Evite repetir código nos testes. Use uma fixture para criar uma conta padrão reutilizável e `@pytest.mark.parametrize` para testar a função `apply_interest()` com vários conjuntos de valores em um único teste.

#### Requisitos
O programa concluído deve:

- Criar uma fixture chamada `account` que retorne um `BankAccount` com saldo inicial de 100 e usá-la em pelo menos 2 testes
- Usar `@pytest.mark.parametrize` em um teste de `apply_interest()` com pelo menos 3 combinações de saldo e taxa
- Executar os testes e obter todos os casos aprovados, mostrando cada combinação na saída de `pytest -v`


### 🛠️ Desafio: Encontrar e Corrigir um Bug

#### Descrição
Uma das regras da conta não está sendo cumprida pelo código atual. Escreva um teste que verifique a regra de negócio, identifique a falha no método responsável, corrija o código e confirme que todos os testes passam.

#### Requisitos
O programa concluído deve:

- Escrever um teste que verifique que uma transferência nunca deixa o saldo da conta de origem negativo
- Executar o teste e registrar, em um comentário no código, o motivo da falha observada
- Corrigir o método responsável no arquivo `bank_account.py`
- Garantir que todos os testes anteriores e o novo teste sejam aprovados com `pytest -v`
