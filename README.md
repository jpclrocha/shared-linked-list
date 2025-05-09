# Simulador de Lista Encadeada Compartilhada em Ambiente Concorrente

Este repositório contém a implementação de um simulador em Python para uma lista encadeada manipulada concorrentemente por múltiplas threads, com o objetivo de demonstrar e analisar problemas clássicos de concorrência como condição de corrida, exclusão mútua, deadlocks e starvation.

## 🎯 Objetivo

- Implementar uma lista encadeada personalizada em Python.
- Simular acessos concorrentes com múltiplas threads realizando operações simultâneas.
- Demonstrar diferenças entre execução com e sem controle de concorrência usando `threading.Lock`.

## 📌 Funcionalidades

- **Operações suportadas pela lista:**
  - Inserção no final
  - Remoção do início
  - Busca de elementos

- **Threads simuladas:**
  - Thread 1: insere 50 elementos
  - Thread 2: insere 50 elementos
  - Thread 3: remove até 60 elementos
  - Thread 4: remove até 60 elementos
  - Thread 5: realiza buscas aleatórias

- **Modos de execução:**
  - Sem lock: demonstra falhas de concorrência (corrida, inconsistência de dados)
  - Com lock: operações sincronizadas garantindo integridade da lista

## 🧰 Tecnologias e Requisitos

- Python 3.x
- `threading.Thread`
- `threading.Lock`
- Implementação manual de lista encadeada (`valor`, `prox`)

## 🔄 Extensões (não obrigatórias)

- Suporte a `multiprocessing`
- Logs com cores e delays artificiais para visualização didática
- Modo visual/debug passo-a-passo

## 📄 Entregáveis

- Código-fonte `.py`
- Relatório de execução `.txt` ou `.pdf` (incluindo descrição do projeto, resultados, fontes consultadas, autoavaliação, etc.)

## 📅 Datas

- Entrega: 11/maio
- Apresentação: 12/maio

## 📚 Conteúdo Integrado

- Estrutura de Dados: Lista Encadeada
- Sistemas Operacionais: Concorrência, sincronização, exclusão mútua

---

**Instituto Federal de Alagoas – IFAL / Campus Maceió**  
Disciplina: Estruturas de Dados e Sistemas Operacionais     
Curso: Bacharelado em Sistemas de Informação
