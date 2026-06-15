# Protótipos de Interface com o Usuário

## Mapa do Site

```mermaid
flowchart TD
    A["Início"] --- B["Criar Roteiro"] & E["Buscar"] & G["Comunidade"] & J["Descobrir"] & N["Cadastro"] & O["Login"] & I["Sobre"] & AA["Roteiros"] & AB["Serviços"] & AC["Parcerias"]
    B --- C["Roteiro rápido"]
    C --- D["Roteiro personalizado"]
    N --- O
    E --- AA & AB
    J --- AA & AB
    G --- H["Publicar"] & H1["Avaliar"] & H2["Denunciar"] & H3["Comentar"]
    H --- O
    H1 --- O
    H2 --- O
    H3 --- O
    AC --- AD["Torne-se um Parceiro"]
    AD --- F2
    O --- P["Rudiero"] & F["Parceiro"]
    P --- P0["Minha Conta"]
    P0 --- R["Meus dados"] & S["Meus roteiros"] & T["Minhas publicações"] & U["Favoritos"] & V["Sair"]
    F --- F0["Minha Conta"]
    F0 --- F1["Meus dados"] & F2["Submeter serviço"] & F3["Meus serviços"] & F4["Sair"]
    I --- L["Quem somos"] & M["Dúvidas"] & a["Privacidade"] & b["Segurança"]
```

## Protótipos de tela

[Link para o projeto no Figma](https://www.figma.com/design/4LHqCSivmd9WjvfWaOOAe7/Rudi%C3%A1---Wireframes?node-id=9-2)

### A. Tela 1: Index

![Index](https://github.com/user-attachments/assets/94863616-5d77-4914-8693-f33b9768b76e)

### B. Tela 2: Descobrir

![Descobrir](https://github.com/user-attachments/assets/ea0cd4f7-375d-4088-951b-7ff8953fadd5)

### C. Tela 3: Comunidade

![Feed](https://github.com/user-attachments/assets/4871c880-a851-4c24-87f2-491c3d545ba0)

### D. Tela 4: Cadastro

![Login](https://github.com/user-attachments/assets/7015ac64-3a25-424d-9ab6-daa217bb0aae)
![Login #2](https://github.com/user-attachments/assets/8039d8a9-2865-4275-8e81-eba12a74f600)

### E. Tela 5: Buscar

![Resultados - Barra](https://github.com/user-attachments/assets/162035aa-2c4c-4da6-b884-8a030a0a0467)
![Resultados - Página](https://github.com/user-attachments/assets/a91c563f-fa69-4116-8319-37a11597377c)

### F. Tela 6: Minha conta (rudiero)

![Minha Conta](https://github.com/user-attachments/assets/a10d39e4-f322-47ce-8b7f-98b8bdc5595e)

### G. Tela 7: Minha conta (parceiro)

![Usuário Parceiro](https://github.com/user-attachments/assets/8dd52894-f9e0-4eed-9d07-e409a708f7bf)

### H. Tela 8: Minha conta (administrador)

![Adm](https://github.com/user-attachments/assets/601dd6d1-0515-4eb5-a76d-1a9679b4bf24)

### I. Tela 9: Roteiro rápido - etapas

![Roteiro rápido etapa 2](https://github.com/user-attachments/assets/b5c57a7f-1ff6-42cd-bfd0-bfadf18a8f94)
![Roteiro rápido etapa 5](https://github.com/user-attachments/assets/e458c8cb-d150-4ac1-9054-ea46bebf27de)

### J. Tela 10: Roteiro completo - etapas

![Roteiro Completo](https://github.com/user-attachments/assets/a3eed091-0592-4fb4-971b-abaebd413b4b)

### K. Tela 11: Resultados - Criação de roteiros

![Result  criação rot  rápido](https://github.com/user-attachments/assets/6f8c0731-bf34-4a42-a61d-7d0e3f159cec)
![Result  da criação de roteiro _ pop up detalhamento](https://github.com/user-attachments/assets/4279d8ad-5da2-4818-85ef-1cbbf213cc67)

### L. Tela 12: Formulário de cadastro de parceiros

![Torne-se um Parceiro](https://github.com/user-attachments/assets/31ee53ba-ffce-4462-af2c-36095d27fb46)

### M. Tela 13: Formulário de cadastro de serviços

![Submeter serviço](https://github.com/user-attachments/assets/74c37421-6e47-4a6a-8e6e-ce792aaaa050)
![Submeter serviço-1](https://github.com/user-attachments/assets/27ff895b-5760-40e2-b8bd-a8a7b73568c9)
