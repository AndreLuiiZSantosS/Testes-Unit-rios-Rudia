# **CDU008. Gerenciar Meus Roteiros**

* **Ator principal**: Rudiero
* **Atores secundários**: -
* **Resumo**: O rudiero, a partir do perfil, consegue utilizar uma ferramenta para editar roteiros com o objetivo de atualizar ou deletar um roteiro próprio.
* **Pré-condição**: O rudiero deve possuir uma conta previamente cadastrada e validada no sistema.
* **Pós-condição**: Os roteiros selecionados pelo rudiero serão atualizados ou deletados da base de dados.

---

## ✅ Fluxo Principal

|                         Ações do ator                        |                                                                Ações do sistema                                                               |
| :----------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------: |
| 0 - Na tela de perfil, ao estar logado, o rudiero clica no botão **"Meus Roteiros"** |- |
| - | 1 - O sistema exibe a página de roteiros pessoais do cliente específico |
| 2 - O rudiero tem a opção de clicar no ícone com 3 pontinhos (mais opções) e selecionar **"Editar Meus Roteiros"** | - |
| - | 3 - O sistema recarrega a mesma página dinamicamente, porém, em cada card de roteiro no perfil do rudiero, irão aparecer dois ícones: um amarelo com um ícone de lápis (update) e um vermelho com um "x" (delete) |
| 4 - O rudiero faz as alterações desejadas nos roteiros escolhidos e depois confirma suas escolhas apertando no botão na parte inferior "Salvar alterações" | - |
|                               -                              | 5 - O sistema atualiza as informações no banco de dados |

---

## 🔁 Fluxo Alternativo I - Rudiero não logado

| Ações do ator |                                                 Ações do sistema                                                 |
| :-----------: | :--------------------------------------------------------------------------------------------------------------: |
|       -       | 0.1 - O sistema identifica que o rudiero não está logado e recarrega a página dinamicamente, apresentando a seguinte mensagem: "Rudiero, faça login para executar essa ação." |

---

## 🔁 Fluxo Alternativo II - O rudiero quer cancelar a edição de roteiros

| Ações do ator |                                                Ações do sistema                                                |
| :-----------: | :------------------------------------------------------------------------------------------------------------: |
| 4.1 - O rudiero percebe que não deseja mais realizar edições em seus roteiros e aperta no botão "Cancelar" na parte inferior, ao lado do botão "Salvar alterações" | - |
| - | 4.2 - O sistema recarrega a página de perfil do rudiero na aba de "Meus Roteiros" |

---



## Diagrama de Interação (Sequência)

-


## Diagrama de Classes de Projeto

-