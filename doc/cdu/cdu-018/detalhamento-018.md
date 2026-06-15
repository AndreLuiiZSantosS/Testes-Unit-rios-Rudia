# **CDU018. Montar Cronograma de Viagem**

* **Ator principal**: Rudiero
* **Atores secundários**: -
* **Resumo**: o Rudiero distribui os serviços selecionados de um roteiro nos dias e horários dentro do período da viagem.
* **Pré-condição**: o roteiro a receber o cronograma deverá estar previamente salvo no sistema.
* **Pós-Condição**: o cronograma de viagem será salvo no roteiro selecionado.

---

## ✅ Fluxo Principal

|                         Ações do ator                        |                                                                Ações do sistema                                                               |
| :----------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------: |
| 0 - Dentro da seção 'editar roteiro', o usuário clica em 'montar cronograma' | - |
| - | 1- O Sistema exibe uma página com os dias da viagem, os serviços do roteiro e os horários de cada dia, das 00:00 às 23:59|
| 2 - O Rudiero seleciona um dia que deseja alocar serviços; por padrão, é exibido o primeiro dia da viagem | - |
| 3 - O Rudiero aloca - arrastando ou clicando - um serviço para um horário do dia selecionado, podendo ajustar a faixa de tempo que pretende disponibilizar para aquela atividade | - |
| 4 - O usuário repete os passos 2 e 3 até estar satisfeito e clica em 'salvar cronograma' | - |
| - | 5 - O Sistema salva o cronograma montado e o vincula ao roteiro referente |

---

## 🔁 Fluxo Alternativo I - 


## Diagrama de Interação (Sequência)


## Diagrama de Classes de Projeto
