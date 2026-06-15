# CDU005. Analisar Proposta de Serviço

- **Ator principal**: Administrador
- **Atores secundários**: -
- **Resumo**: Analisar propostas de novos serviços submetidos por usuários parceiros.
- **Pré-condição**: O usuário parceiro enviar uma proposta de serviço.
- **Pós-Condição**: A proposta é aceita e o serviço fica disponível para a criação de roteiros.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 0 - No perfil, o administrador acessa a aba de serviços em análise | - |  
| - | 1 - O sistema apresenta as propostas de novos serviços aguardando análise |
| 2 - O administrador seleciona um serviço | - |
| - | 3 - O sistema apresenta os dados do serviço que foram fornecidos pelo usuário parceiro |
| 4 - O administrador analisa a proposta | - |
| 5 - O administrador aceita a proposta | - |
| - | 6 - O status do serviço é atualizado para 'aprovado' e um e-mail de confirmação é enviado para o usuário parceiro que cadastrou o serviço |
| - | 7 - O sistema atualiza a lista de serviços e o disponibiliza para a criação de novos roteiros |  

## Fluxo Alternativo I - Proposta Recusada
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 5.1 - O administrador recusa a proposta | - |  
| - | 5.2 - O sistema solicita ao administrador o(s) motivo(s) da reijeição da proposta |
| 5.3 - O administrador informa o(s) motivo(s) | - |
| - | 5.4 - O status do serviço é atualizado para 'recusado' e um e-mail é enviado para o parceiro autor da proposta informando o(s) motivo(s) apontado(s) pelo administrador |

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...