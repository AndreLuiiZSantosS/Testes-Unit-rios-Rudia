# CDU004. Submeter Proposta de Parceria 

- **Ator principal**: Visitante
- **Atores secundários**: Administrador	 
- **Resumo**: Registro de submissões de proposta de parcerias comerciais
- **Pré-condição**: O visitante deve estar de acordo com as políticas e termos de uso da plataforma 
- **Pós-Condição**: A proposta de parceria é submetida e aguarda a análise por parte dos administradores

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 0 - na tela inicial, o visitante navega até o rodapé e clica na opção 'torne-se um parceiro' | - |  
| - | 1 - o sistema exibe a página de proposta de parcerias e fornece o formulário de submissão de proposta de parceria |
| 2 - o visitante preenche o formulário e submete a proposta de parceria | - |
| - | 3 - a submissão é realizada e um link para acompanhamento do status da proposta é enviado por e-mail ao proponente |
| - | 4 - a lista de propostas em análise é atualizada incluindo a nova proposta e o sistema direciona o usuário para a página de submissão de serviços |

## Fluxo Alternativo I - Dados Inválidos
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| - | 3.1 - o sistema informa que um ou mais dados (e-mail, cpf, cnpj, etc.) é/são inválido(s) e solicita a correção (retorna ao passo 2) | 

## Fluxo Alternativo II - Dados já Persistidos
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| - | 3.2 - o sistema informa que um ou mais dados (e-mail, cpf, cnpj, etc.) já está/estão registrados e solicita a correção (retorna ao passo 2) |  

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

![Diagrama de sequência](<CDU004 - Diagrama_de_sequencia.png>)

## Diagrama de Classes de Projeto

![Diagrama de classes de Projeto](<CDU 004 - Diagrama_classes_projeto.png>)