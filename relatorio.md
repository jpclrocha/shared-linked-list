OBS: Esse arquivo contém o mesmo conteúdo do txt, porém com visualização facilitada

Instituto Federal de Alagoas – IFAL / Campus Maceió  
Disciplina: Estruturas de Dados e Sistemas Operacionais     
Curso: Bacharelado em Sistemas de Informação    
Alunos: João Pedro de Castro Laranjeira Rocha e Daniel do Carmo Nascimento

# Relatório de Desempenho – Lista Encadeada Compartilhada

## Discussão sobre a construção do projeto

O projeto consistiu na implementação de uma lista encadeada simples com duas variações:
- **Sem controle de concorrência**.
- **Com controle de concorrência usando `threading.Lock`**.

Foram implementadas as operações:
  - **Inserção no final**
  - **Remoção do início**
  - **Busca de elementos**

Decisões principais:
- Estrutura básica e não ordenada para foco nas operações (`insert`, `remove`, `search`) e na concorrência.
- Uso de ponteiros `head` e `tail` para garantir tempo constante nas operações de inserção no início e no fim da lista.
- Uso de lock em todas as operações da versão concorrente, priorizando integridade mesmo com possível perda de desempenho.
- Interfaces idênticas entre as duas versões para facilitar comparação.

Tecnologias utilizadas
- Python 3
- `threading.Thread`
- `threading.Lock`
- Implementação manual de lista encadeada (Nodes com `data`, `next`)

Também implementamos extensões recomendadas  

- Logs com cores e delays artificiais para visualização didática
- Modo visual/debug passo-a-passo

## Discussão sobre os resultados da execução do projeto

Foram realizados testes com múltiplas threads (5, como pedido, e 1000, à propósitos de teste de estresse) executando operações pré-determinadas e reprodutíveis.

### Resultados:

- **Versão sem lock**:
  - Resultados inconsistentes.
  - Múltiplas operações executadas ao mesmo tempo, sem qualquer tipo de bloqueio
  - Tempo médio ~0.26s.

- **Versão com lock**:
  - Comportamento determinístico.
  - Uma operação é executada por vez.
  - Integridade da estrutura preservada.
  - Tempo médio ~0.46s.

A diferença de desempenho foi observada, como esperado, devido à serialização das operações provocada pelos locks. Como utilizamos os ponteiros de `head` e `tail`, a lista não quebra com frequência e não temos problemas de índices e ponteiros quebrados. Porém, é possível observar que na implementação sem lock várias operações são iniciadas ao mesmo tempo, sem que uma operação que ocorreu primeiro tenha terminado sua execução. Na lista com lock isso não ocorre, e podemos observar isso com os logs

## Conteúdo consultado

- Documentação oficial do Python (`threading`, `random`, `time`)
- Artigos e materiais:
  - https://en.wikipedia.org/wiki/Concurrent_data_structure
  - https://realpython.com/intro-to-python-threading/
  - https://stackoverflow.com/questions/1312331/what-is-the-cost-of-a-lock-in-python
  - https://docs.python.org/3/library/threading.html
  - https://www.w3schools.com/python/ref_random_randint.asp
  - https://www.pythontutorial.net/python-concurrency/python-threading-lock/
  - https://www.youtube.com/watch?v=jIM87UqOq3g

## Autoavaliação da equipe

- Estrutura funcional, limpa e clara.
- Domínio dos conceitos básicos de concorrência.
- Separação lógica e modularidade mantidas.

### Conclusão: entregas realizadas

- Todas as operações foram implementadas corretamente.
- Testes comparativos.

### Comentários finais

#### Dificuldades:
- Testes paralelos controlados sem dependências externas.
- Limitações impostas pelo GIL em Python.

#### Melhorias possíveis:
- Implementação sem tail, para ver a lista realmente quebrar sem locks
- Benchmarking mais robusto.