# ADR-001: Escolha da Arquitetura para o Sistema de Gestão de Equipamentos

**Status:** Aceito  
**Data:** 28/04/2026

## Contexto

A versão 1.0 do sistema foi desenvolvida como um script único, o que resultou em falhas estruturais e impediu o atendimento de requisitos não funcionais fundamentais para a evolução do projeto:

- **RNF03 (Manutenibilidade):** A adição de um novo tipo de equipamento exige a modificação de múltiplos trechos de código em um único arquivo, aumentando o risco de erros.
- **RNF04 (Testabilidade):** Não é possível testar as regras de negócio sem depender de entradas manuais do usuário (`input`) ou da existência de arquivos físicos de dados.

O sistema utiliza uma interface de linha de comando (CLI) e deve ser mantido por uma equipe iniciante.

## Opções consideradas

| Critério                                                     | Arquivo único | Em camadas    | MVC         |
|---------------|---------------|---------------|--------------|
| Atende RNF03 (novo tipo sem modificar múltiplos módulos)?    | Não           | **Sim**       | **Sim**     |
| Atende RNF04 (testar regras sem estado externo)?             | Não           | **Sim**       | **Sim**     |
| Adequado para CLI sem interface gráfica?                     | Sim           | **Sim**       | Não         |
| Familiar para equipe iniciante?                              | Sim           | **Sim**       | Não         |

- **Arquivo único:** descartado — os problemas de acoplamento e falta de testes persistem, tornando o sistema insustentável.
- **MVC:** descartado — focado em interfaces baseadas em eventos (gráficas/web); para um sistema CLI, traria uma complexidade desnecessária para a equipe.
- **Em camadas:** escolhido — resolve a separação de responsabilidades de forma clara, garantindo que a lógica de negócio seja independente da interface e dos arquivos de dados.

## Decisão

Adotaremos a **Arquitetura em Camadas** para isolar as responsabilidades em módulos distintos:

- `/interação` — Lida exclusivamente com a interface CLI (menus, `print` e captura de `input`).
- `/domínio` — Contém as regras de negócio puras e as definições de cada tipo de equipamento (garante o atendimento ao **RNF03** e **RNF04**).
- `/data` — Camada de persistência responsável por ler e gravar os dados em arquivos externos.

## Consequências

- **Melhoria na manutenção:** Adicionar um novo tipo de equipamento exige alteração apenas em um módulo dentro de `/domínio`, sem afetar as outras partes do sistema.
- **Melhoria na testabilidade:** As regras de negócio em `/domínio` podem ser testadas através de scripts automatizados sem necessidade de interação humana ou arquivos reais.
- **Curva de aprendizado:** Embora gere mais arquivos que a versão anterior, a estrutura clara ajuda a equipe iniciante a saber exatamente onde cada nova funcionalidade deve ser implementada.
