# CDU006. Analisar Proposta de Parceria

- **Ator principal**: Administrador
- **Atores secundários**: -
- **Resumo**: Analisar propostas de novos usuários visitantes para a criação de perfil de parceiro na aplicação.
- **Pré-condição**: O usuário visitante enviar uma proposta de parceria.
- **Pós-Condição**: A proposta é aceita e a conta é criada na aplicação.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 0 - No perfil, o administrador acessa a aba de propostas submetidas | - |  
| - | 1 - O sistema apresenta as propostas de parceria submetidas |
| 2 - O administrador seleciona uma proposta | - |
| - | 3 - O sistema apresenta os dados da proposta fornecida pelo visitante |
| 4 - O administrador analisa a proposta | - |
| 5 - O administrador aceita a proposta | - |
| - | 6 - O status da proposta é atualizado para 'aceita' e um e-mail de confirmação é enviado para o proponente da parceria |
| - | 7 - O sistema persiste os dados do novo parceiro e cria a conta de usuário parceiro |  

## Fluxo Alternativo I - Proposta Recusada
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 5.1 - O administrador recusa a proposta | - |  
| - | 5.2 - O sistema solicita ao administrador o(s) motivo(s) da reijeição da proposta |
| 5.3 - O administrador informa o(s) motivo(s) | - |
| - | 5.4 - O status da proposta é atualizado para 'recusada' e um e-mail é enviado para o autor da proposta informando o(s) motivo(s) apontado(s) pelo administrador |

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

![Diagrama de sequência](<diagrama_sequencia_CDU_006.png>)

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...