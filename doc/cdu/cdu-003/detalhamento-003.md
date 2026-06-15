# CDU003. Submeter Proposta de Serviço

- **Ator principal**: Visitante, Parceiro
- **Atores secundários**: Administrador 
- **Resumo**: Registro de submissões de propostas de serviços para a criação de roteiros
- **Pré-condição**: O usuário deve antes submeter a proposta de parceria
- **Pós-Condição**: A proposta de serviço é submetida e aguarda a análise por parte dos administradores

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 0 - na página de parcerias, após submeter a proposta de parceria, o visitante (possível novo parceiro) seleciona a opção 'submeter serviço' | - |  
| - | 1 - o sistema exibe a página de cadastro de novos serviços e fornece o formulário de submissão de novos serviços |
| 2 - o visitante preenche o formulário e submete o novo serviço | - | 
| - | 3 - a submissão é realizada e um documento contendo um código de validação é enviado via correios para o endereço informado no formulário | 
| - | 4 - a lista de serviços em análise é atualizada, incluindo o novo serviço e o status da proposta fica como 'aguardando confirmação de endereço' | 

## Fluxo Alternativo I - Novos Serviços
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 0.1 - ao logar-se em sua conta, o usuário parceiro acessa seu perfil de usuário e na seção de serviços do usuário, seleciona a opção 'novo serviço' | - |  
| - | 0.2 - o sistema exibe a página de cadastro de novos serviços e fornece o formulário de submissão de novos serviços (retorna ao passo 1) |

## Fluxo Alternativo II - Dados Inválidos
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| - | 3.1 - o sistema informa que um ou mais dados (e-mail, cpf, cnpj, etc.) é/são inválido(s) e solicita a correção (retorna ao passo 2) | 

## Fluxo Alternativo III - Dados já Persistidos
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| - | 3.2 - o sistema informa que um ou mais dados (e-mail, cpf, cnpj, etc.) já está/estão registrados e solicita a correção (retorna ao passo 2) |  

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...