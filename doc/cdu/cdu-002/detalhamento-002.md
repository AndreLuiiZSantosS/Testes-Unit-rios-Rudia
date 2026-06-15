# CDU002. Criar Roteiro Rápido

- **Ator principal**: Visitante, Membro
- **Atores secundários**: Parceiro
- **Resumo**: Elaboração de roteiro por meio de respostas a um breve questionário
- **Pré-condição**: -
- **Pós-Condição**: Roteiro criado com sucesso com as sugestões baseadas nas respostas fornecidas pelo ator

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 0 - na tela inicial, o ator seleciona o campo de texto 'para onde você quer ir' e responde a pergunta inicial do questionário | - |  
| - | 1 - o sistema exibe a página de roteiro rápido com um fluxo de perguntas que devem ser respondidas de forma sequencial |
| 2 - o ator responde as perguntas do questionário | - |
| - | 3 - o sistema exibe as respostas fornecidas pelo ator e solicita confirmação para seguir com a criação do roteiro |
| 4 - o ator confirma as informções | - |
| - | 5 - o sistema cria 3 opções de roteiro para escolha baseando-se nas respostas fornecidas pelo ator e concede a opção de personalizar roteiro |
| 6 - o ator escolhe uma das 3 opções sugeridas | - |

## Fluxo Alternativo I - Editar respostas
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 4.1 - o ator seleciona a opção de editar uma de suas respostas | - |  
| - | 4.2 - o sistema o direciona para a opção selecionada (retorna ao passo 2) |

## Fluxo Alternativo II - Personalizar roteiro
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 6.1 - o ator escolhe a opção de personalizar roteiro | - |  
| - | 6.2 - o sistema o direciona para 'criar roteiro personalizado' (cdu 005) |  

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...
