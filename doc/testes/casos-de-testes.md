# 1 Introdução

Este documento reúne os casos de teste elaborados para validar os principais fluxos da aplicação Rudiá, desenvolvida no contexto do PDS Corporativo. Os testes aqui descritos abrangem diferentes casos de uso da aplicação, com o objetivo de assegurar que cada funcionalidade opere conforme os requisitos definidos.

Cada caso de teste inclui informações detalhadas sobre o cenário a ser avaliado, os dados de entrada necessários e resultados esperados.

## 1.1 Visão geral

O documento foi estruturado para garantir clareza e facilitar a consulta aos testes da aplicação Rudiá. Ele apresenta a introdução ao propósito dos testes, uma visão geral dos critérios de seleção dos casos de uso e, por fim, os testes funcionais com seus respectivos cenários, dados e resultados esperados, servindo como referência para as equipes de desenvolvimento e qualidade. <br> <br>
|-🗂️ **1 Introdução** <br>
| |- 📑 1.1 Visão geral <br>
|- 🗂️ **2 Histórico de Revisões** <br>
|- 🗂️ **3 Testes Funcionais** <br>

## Histórico de Revisões

|    Data    | Versão |            Descrição            |      Autores      |
| :--------: | :----: | :-----------------------------: | :---------------: |
| 20/04/2026 |  1.0   |         Versão inicial          | André, Isaac, João Vitor, Lucas, Marcos e Pedro |


## Testes Funcionais

### CDU 001 - Criar Viagem Personalizada

#### Fluxo Principal

| Nº | Destino | Dias | Viajantes | Hospedagem | Lazer | Alimentação | Transporte | Nome | Descrição | Visibilidade | Resultado Esperado | Resultado Obtido | Status |
|----|---------|------|-----------|------------|-------|-------------|------------|------|-----------|--------------|--------------------|------------------|--------|
| 01 | Natal | 3 | (adultos 2, crianças 1) | 1 | 1 | 1 | 1 | Rota Nordeste | Planejamento completo de viagem | PUBLICO | ✅ Viagem Criada com Sucesso | - | - | 
| 02 | (vazio) | 4 | (adultos 2, crianças 2) | 1 | 1 | 1 | 1 | Trip RN Legal | Descrição válida de passeio | PUBLICO | ❌ Destino obrigatório | - | - |
| 03 | ### | 2 | (adultos 3, crianças 0) | 1 | 1 | 1 | 1 | Jornada Litoral | Viagem com amigos no litoral | PUBLICO | ❌ Destino inválido | - | - |
| 04 | Mossoró | 1 | (adultos 1, crianças 1) | 1 | 1 | 1 | 1 | Viagem Mossoró | Explorar cultura e passeios locais | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 05 | Parnamirim | 0 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Trip Parnamirim | Passeio urbano planejado | PUBLICO | ❌ Dias deve ser > 0 | - | - |
| 06 | Caicó | -3 | (adultos 2, crianças 1) | 1 | 1 | 1 | 1 | Roteiro Seridó | Cultura regional e gastronomia | PUBLICO | ❌ Dias inválido | - | - |
| 07 | Assú | 365 | (adultos 4, crianças 2) | 1 | 1 | 1 | 1 | Ano Completo RN | Viagem longa bem estruturada | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 08 | Currais Novos | 1 | (adultos 1, crianças 0) | 1 | 1 | 1 | 1 | Solo Seridó Trip | Experiência individual planejada | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 09 | Pau dos Ferros | 2 | (adultos 1, crianças 3) | 1 | 1 | 1 | 1 | Família Oeste RN | Viagem com foco familiar | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 10 | Natal | 1 | (adultos 0, crianças 2) | 1 | 1 | 1 | 1 | Kids Tour RN | Passeio sem responsável adulto | PUBLICO | ❌ Mínimo 1 adulto | - | - |
| 11 | Mossoró | 1 | (adultos 0, crianças 0) | 1 | 1 | 1 | 1 | Viagem Nula RN | Nenhum participante definido | PUBLICO | ❌ Pelo menos 1 viajante | - | - |
| 12 | Parnamirim | 1 | (adultos -1, crianças 1) | 1 | 1 | 1 | 1 | Adulto Inválido | Teste de valor negativo adulto | PUBLICO | ❌ Adultos inválido | - | - |
| 13 | Caicó | 1 | (adultos 1, crianças -2) | 1 | 1 | 1 | 1 | Criança Inválida | Teste de valor negativo criança | PUBLICO | ❌ Crianças inválido | - | - |
| 14 | Assú | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Casal Interior RN | Viagem em casal planejada | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 15 | Currais Novos | 2 | (adultos 2, crianças 1) | 0 | 1 | 1 | 1 | Sem Estadia RN | Falta de hospedagem | PUBLICO | ❌ Hospedagem obrigatória | - | - |
| 16 | Pau dos Ferros | 2 | (adultos 2, crianças 1) | 2 | 1 | 1 | 1 | Duplo Hotel RN | Seleção inválida de hospedagem | PUBLICO | ❌ Apenas 1 hospedagem | - | - |
| 17 | Natal | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Viagem Completa RN | Planejamento equilibrado geral | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 18 | Mossoró | 2 | (adultos 2, crianças 0) | 1 | 0 | 1 | 1 | Sem Lazer RN | Falta de atividades | PUBLICO | ❌ Mínimo 1 lazer | - | - |
| 19 | Parnamirim | 2 | (adultos 2, crianças 0) | 1 | 3 | 1 | 1 | Lazer Total RN | Diversas opções selecionadas | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 20 | Caicó | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Roteiro Cultural RN | Turismo regional completo | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 21 | Assú | 2 | (adultos 2, crianças 0) | 1 | 1 | 0 | 1 | Sem Refeição RN | Nenhum serviço alimentar | PUBLICO | ❌ Mínimo 1 alimentação | - | - |
| 22 | Currais Novos | 2 | (adultos 2, crianças 0) | 1 | 1 | 4 | 1 | Food Experience RN | Experiência gastronômica | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 23 | Pau dos Ferros | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Viagem OK RN | Fluxo padrão completo | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 24 | Natal | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 0 | Sem Transporte RN | Falta de deslocamento | PUBLICO | ❌ Transporte obrigatório | - | - |
| 25 | Mossoró | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 2 | Transporte Duplicado | Seleção inválida | PUBLICO | ❌ Apenas 1 transporte | - | - |
| 26 | Parnamirim | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | ABCD | Descrição válida completa aqui | PUBLICO | ❌ Nome < 5 caracteres | - | - |
| 27 | Caicó | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | ABCDE | Descrição válida completa aqui | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 28 | Assú | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Viagem completa pelo interior do Rio Grande do Norte explorando cultura local, gastronomia típica e pontos turísticos históricos da região | Descrição válida completa aqui | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 29 | Currais Novos | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Viagem completa pelo interior do Rio Grande do Norte explorando cultura local, gastronomia típica e pontos turísticos históricos da região com roteiro adicional | Descrição válida completa aqui | PUBLICO | ❌ Nome > 150 caracteres | - | - |
| 30 | Pau dos Ferros | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Plano Oeste RN | Curta | PUBLICO | ❌ Descrição < 10 caracteres | - | - |
| 31 | Natal | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Plano Completo RN | 1234567890 | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 32 | Mossoró | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Plano Longo RN | Viagem cuidadosamente planejada com roteiro detalhado incluindo hospedagem confortável, opções variadas de lazer, alimentação regional e transporte organizado para todos os dias da estadia garantindo uma experiência completa e tranquila para todos os participantes envolvidos no planejamento da viagem | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 33 | Parnamirim | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Plano Excedente RN | Viagem cuidadosamente planejada com roteiro detalhado incluindo hospedagem confortável, opções variadas de lazer, alimentação regional e transporte organizado para todos os dias da estadia garantindo uma experiência completa e tranquila para todos os participantes envolvidos no planejamento da viagem com adição de informações extras que ultrapassam o limite permitido pelo sistema | PUBLICO | ❌ Descrição > 500 caracteres | - | - |
| 34 | Natal | 2 | (adultos 2, crianças 1) | 1 | 1 | 1 | 1 | Roteiro Praias RN | Viagem planejada com foco em descanso e lazer | PUBLICO | ✅ Viagem Criada com Sucesso | - | - |
| 35 | Mossoró | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Tour Cultural RN | Exploração de pontos históricos e culturais | PRIVADO | ✅ Viagem Criada com Sucesso | - | - |
| 36 | Parnamirim | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Viagem Urbana RN | Planejamento de passeio urbano completo | (vazio) | ❌ Visibilidade inválida | - | - |
| 37 | Currais Novos | 2 | (adultos 2, crianças 0) | 1 | 1 | 1 | 1 | Viagem Alternativa RN | Roteiro alternativo com experiências locais | AMIGOS | ❌ Visibilidade inválida (fora do domínio) | - | - |

### CDU 003 - Submeter Proposta de Serviço

#### Testes Funcionais

| Nº  | Nome               | Descrição | Preço Min | Preço Max | Capacidade | CEP      | Logradouro | Número | Cidade      | Estado        | Categoria | Tags         | Horário Abertura | Horário Fechamento | Dias    | Fotos           | Resultado Esperado       | Resultado Obtido | Status |
| --- | ------------------ | ----------------------- | --------- | --------- | ---------- | -------- | ---------- | ------ | ----------- | ------------- | --------- | ------------ | ----------- | ------- | --------------- | ------------------------ | ---------------- | ------- | ------ |
| 01  | Empresa Alpha LTDA | Serviço completo válido | 100       | 200       | 50         | 59123456 | Rua A      | 100    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["SEG"] | 1 imagem válida | ✅ Sucesso               | -                | -      |
| 02  | (vazio)            | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua B      | 101    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["TER"] | 1 imagem válida | ❌ Nome obrigatório      | -                | -      |
| 03  | Empresa Gama       | Serviço válido          | (vazio)   | 200       | 50         | 59123456 | Rua D      | 103    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["QUI"] | 1 imagem válida | ❌ Preço mínimo obrigatório | -             | -      |
| 04  | Empresa Delta      | Serviço válido          | 100       | 50        | 50         | 59123456 | Rua E      | 104    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["SEX"] | 1 imagem válida | ❌ Preço máximo < mínimo | -                | -      |
| 05  | Empresa Épsilon    | Serviço válido          | 100       | 200       | 10.5       | 59123456 | Rua F      | 105    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["SAB"] | 1 imagem válida | ❌ Capacidade inválida   | -                | -      |
| 06  | Empresa Zeta       | Serviço válido          | 100       | 200       | 50         | 1234     | Rua G      | 106    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["DOM"] | 1 imagem válida | ❌ CEP inválido          | -                | -      |
| 07  | Empresa Eta        | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua H      | 107    | ID inválido | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["SEG"] | 1 imagem válida | ❌ Cidade inexistente    | -                | -      |
| 08  | Empresa Theta      | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua I      | 108    | ID válido   | Coerente      | ID inválido | Lista válida | 08:00 | 18:00 | ["TER"] | 1 imagem válida | ❌ Categoria inexistente | -                | -      |
| 09  | Empresa Iota       | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua J      | 109    | ID válido   | Coerente      | ID válido | Tag inválida | 08:00 | 18:00 | ["QUA"] | 1 imagem válida | ❌ Tags inválidas        | -                | -      |
| 10  | Empresa Kappa      | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua K      | 110    | ID válido   | Coerente      | ID válido | Lista válida | 18:00 | 18:00 | ["QUI"] | 1 imagem válida | ❌ Horário inválido      | -                | -      |
| 11  | Empresa Lambda     | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua L      | 111    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["SEX"] | Sem imagem      | ❌ Foto obrigatória      | -                | -      |
| 12  | Empresa Mu         | (vazio)                 | 100       | 200       | 50         | 59123456 | Rua M      | 112    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["SEG"] | 1 imagem válida | ❌ Descrição obrigatória | -                | -      |
| 13  | Empresa Nu         | Serviço válido          | 100       | (vazio)   | 50         | 59123456 | Rua N      | 113    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["TER"] | 1 imagem válida | ❌ Preço máximo obrigatório | -             | -      |
| 14  | Empresa Xi         | Serviço válido          | 100       | 200       | 0          | 59123456 | Rua O      | 114    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["QUA"] | 1 imagem válida | ❌ Capacidade deve ser > 0 | -             | -      |
| 15  | Empresa Omicron    | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua A      | 100    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["QUI"] | 1 imagem válida | ❌ Endereço já cadastrado | -               | -      |
| 16  | Empresa Pi         | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua P      | ABC    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["SEX"] | 1 imagem válida | ❌ Número inválido       | -                | -      |
| 17  | Empresa Rho        | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua Q      | 115    | ID válido   | Coerente      | ID válido | (vazio)      | 08:00 | 18:00 | ["SAB"] | 1 imagem válida | ❌ Tags obrigatórias     | -                | -      |
| 18  | Empresa Sigma      | Serviço válido          | 100       | 200       | 50         | (vazio)  | (vazio)    | (vazio) | ID válido | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["DOM"] | 1 imagem válida | ❌ Endereço obrigatório  | -                | -      |
| 19  | Empresa Tau        | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua R      | 116    | ID válido   | Coerente      | ID válido | Lista válida | (vazio) | (vazio) | (vazio) | 1 imagem válida | ❌ Horários obrigatórios | -                | -      |
| 20  | Empresa Upsilon    | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua S      | 117    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["XYZ"] | 1 imagem válida | ❌ Dia da semana inválido | -              | -      |
| 21  | Empresa Phi        | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua T      | 118    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["SEG", "SEG"] | 1 imagem válida | ❌ Dias duplicados | -            | -      |
| 22  | Empresa Chi        | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua U      | 119    | (vazio)     | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["TER"] | 1 imagem válida | ❌ Cidade obrigatória    | -                | -      |
| 23  | Empresa Psi        | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua V      | 120    | ID válido   | Coerente      | (vazio)   | Lista válida | 08:00 | 18:00 | ["QUA"] | 1 imagem válida | ❌ Categoria obrigatória | -                | -      |
| 24  | Empresa Omega      | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua W      | 121    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["QUI"] | Base64 inválida | ❌ Imagem inválida        | -               | -      |
| 25  | Empresa Alpha LTDA | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua X      | 122    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["SEX"] | 1 imagem válida | ❌ Nome já cadastrado para o parceiro | -     | -      |
| 26  | Nome com 256 caracteres | Serviço válido     | 100       | 200       | 50         | 59123456 | Rua Y      | 123    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["SAB"] | 1 imagem válida | ❌ Nome excede 255 caracteres | -          | -      |
| 27  | Empresa Zeta 2     | Serviço válido          | 100       | 200       | 50         | 59123456 | Logradouro com 256 caracteres | 124 | ID válido | Coerente | ID válido | Lista válida | 08:00 | 18:00 | ["DOM"] | 1 imagem válida | ❌ Logradouro excede 255 caracteres | -   | -      |
| 28  | Empresa Eta 2      | Serviço válido          | 100       | 200       | 50         | 59123456 | Rua Z      | 12345678901 | ID válido | Coerente | ID válido | Lista válida | 08:00 | 18:00 | ["SEG"] | 1 imagem válida | ❌ Número excede 10 caracteres | -        | -      |
| 29  | Empresa Theta 2    | Serviço válido          | 100.999   | 200       | 50         | 59123456 | Rua AA     | 125    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["TER"] | 1 imagem válida | ❌ Preço mínimo com mais de 2 casas decimais | - | - |
| 30  | Empresa Iota 2     | Serviço válido          | 100       | 10000000000 | 50       | 59123456 | Rua AB     | 126    | ID válido   | Coerente      | ID válido | Lista válida | 08:00 | 18:00 | ["QUA"] | 1 imagem válida | ❌ Preço máximo excede 10 dígitos | -      | -      |

### CDU 004 - Submeter Proposta de Parceria

#### Fluxo Principal

| Nome                | Nome de usuário       | Senha          | Confirmação de senha   | Email                      | Telefone         | Estado   | Cidade    | CNPJ            | Resultado Esperado                                  | Resultado Obtido   | Situação   |
|:--------------------|:----------------------|:---------------|:-----------------------|:---------------------------|:-----------------|:---------|:----------|:----------------|:----------------------------------------------------|:-------------------|:-----------|
| brisadomar          | Hotel Brisa do Mar    | SenhaForte123! | SenhaForte123!         | contato@brisadomar.com     | 84999999999      | RN       | Natal     | 97321847000100  | Cadastro realizado com sucesso.                     | -                  | -          |
| bomgostorestaurante | Restaurante Bom Gosto | SenhaForte123! | SenhaForte123!         | contato@bomgosto.com       | -                | RN       | Natal     | 57964232000187  | Cadastro realizado com sucesso.                     | -                  | -          |
| brisadomar          | Hotel Brisa do Mar    | SenhaForte123! | SenhaForte123!         | atendimento@brisadomar.com | -                | RN       | Natal     | 10219444000176  | Erro (nome de usuário em uso).                      | -                  | -          |
| brisadomar2         | Hotel Brisa do Mar    | SenhaForte123! | SenhaForte123!         | contato@brisadomar.com     | -                | RN       | Natal     | 5256573000102   | Erro (e-mail em uso).                               | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | contatobuggytour.com       | -                | RN       | Natal     | 90178186000166  | Erro de validação de e-mail.                        | -                  | -          |
| brisadomar2         | Hotel Brisa do Mar    | SenhaForte123! | SenhaForte123!         | atendimento@brisadomar.com | -                | RN       | Natal     | 97321847000100  | Erro (CNPJ em uso).                                 | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | contato@buggytour.com      | -                | RN       | Natal     | 123456780001000 | Erro (CNPJ excedeu limite).                         | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte321!         | contato@buggytour.com      | -                | RN       | Natal     | 90178186000166  | Erro (Senhas não coincidem).                        | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | contato@buggytour.com      | 84999999999      | RN       | Natal     | 90178186000166  | Erro (Telefone em uso).                             | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | contato@buggytour.com      | 1199999999999999 | RN       | Natal     | 90178186000166  | Erro (Telefone excedeu limite).                     | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | contato@buggytour.com      | -                | HL       | Natal     | 90178186000166  | Erro (Estado inválido).                             | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | contato@buggytour.com      | -                | RN       | São Paulo | 90178186000166  | Erro (Cidade não pertence ao estado).               | -                  | -          |
| -                   | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | contato@buggytour.com      | 84998877556      | RN       | Natal     | 90178186000166  | Erro (Nome é obrigatório)                           | -                  | -          |
| buggytour           | -                     | SenhaForte123! | SenhaForte123!         | contato@buggytour.com      | 84998877556      | RN       | Natal     | 90178186000166  | Erro (Nome de usuário é obrigatório)                | -                  | -          |
| buggytour           | Buggy Tour Passeios   | -              | SenhaForte123!         | contato@buggytour.com      | 84998877556      | RN       | Natal     | 90178186000166  | Erro (Senha é obrigatória)                          | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | -                      | contato@buggytour.com      | 84998877556      | RN       | Natal     | 90178186000166  | Erro (Confirmação obrigatória/Senhas não coincidem) | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | -                          | 84998877556      | RN       | Natal     | 90178186000166  | Erro (Email é obrigatório)                          | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | contato@buggytour.com      | 84998877556      | -        | Natal     | 90178186000166  | Erro (Estado é obrigatório)                         | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | contato@buggytour.com      | 84998877556      | RN       | -         | 90178186000166  | Erro (Cidade é obrigatória)                         | -                  | -          |
| buggytour           | Buggy Tour Passeios   | SenhaForte123! | SenhaForte123!         | contato@buggytour.com      | 84998877556      | RN       | Natal     | -               | Erro (CNPJ é obrigatório)                           | -                  | -          |

### CDU 005 - Analisar Proposta de Serviço

#### Fluxo Principal

| Entrada 1 (Acesso/Fila) | Entrada 2 (Seleção/Visualização) | Entrada 3 (Ação do Admin) | Entrada 4 (Motivo Rejeição) | Entrada 5 (Confirmação/Ambiente) | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Perfil Administrador autenticado. Fila possui propostas. | Proposta P1 selecionada. Dados do serviço íntegros. | Botão "Aprovar" acionado. | N/A (Campo oculto ou não exigido). | Confirmar Operação (SMTP ativo). | Status da P1 alterado para 'aprovado'. Serviço disponibilizado e e-mail de sucesso enviado. |
| Perfil Administrador autenticado. Fila possui propostas. | Proposta P2 selecionada. Dados renderizados íntegros. | Botão "Recusar" acionado. | "A infraestrutura relatada não atende aos padrões de segurança ISO..." | Confirmar Operação (SMTP ativo). | Status da P2 alterado para 'recusado'. E-mail enviado contendo o texto da Entrada 4 na íntegra. |
| Perfil Administrador autenticado. Fila possui propostas. | Proposta P3 selecionada. Dados renderizados íntegros. | Botão "Recusar" acionado. | [Vazio] | Confirmar Operação. | Transação abortada. Erro: "Motivo da rejeição é obrigatório". Status permanece 'em análise'. |
| Perfil Usuário Parceiro autenticado (Autor). | Tentativa de acesso direto à URL administrativa. | N/A | N/A | N/A | Acesso negado. Erro HTTP 403 (Forbidden) / Redirecionamento de segurança. |
| Perfil Administrador autenticado. Fila Vazia. | N/A (Nenhuma proposta listada). | N/A | N/A | N/A | Exibição de mensagem: "Não há serviços em análise no momento". Interações inativadas. |
| Perfil Administrador autenticado. Fila possui propostas. | Proposta P4 selecionada. Dados exibidos. | Botão "Aprovar" acionado. | Inserção por manipulação de DOM de texto em campo oculto. | Confirmar Operação. | Status da P4 alterado para 'aprovado'. Texto injetado indevidamente ignorado pelo back-end. |
| Perfil Administrador autenticado. Fila possui propostas. | Proposta P5 selecionada. | Botão "Recusar" acionado. | Texto inserido com 10.000 caracteres (excesso de limite). | Confirmar Operação. | Erro de validação de limite. Sistema impede falha de BD e avisa sobre limite de caracteres. |
| Perfil Administrador autenticado. Fila possui propostas. | P6 já aprovada em outra aba simultaneamente. | Botão "Aprovar" acionado. | N/A | Confirmar Operação. | Erro de Concorrência. Rejeição da requisição por alteração prévia de status. Lista é atualizada. |
| Perfil Administrador autenticado. Fila possui propostas. | Proposta P7 selecionada. | Botão "Aprovar" acionado. | N/A | Confirmar Operação. Falha simulada no SMTP. | Status alterado para 'aprovado'. Erro de e-mail não reverte aprovação; gera alerta para retentativa. |

### CDU 007 - Auto Cadastro

#### Fluxo Principal

| Nome de usuário | Nome | Email | Senha | Confirmação de senha | Resultado Esperado | Resultado Obtido | Situação |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| anasilva | Ana Silva | ana@email.com | SenhaForte1! | SenhaForte1! | Cadastro realizado com sucesso. | - | - |
| joaopaulo | João Paulo | joao@email.com | SenhaForte1! | SenhaForte1! | Erro (Nome de usuário já está em uso). | - | - |
| mariacosta | Maria Costa | ana@email.com | SenhaForte1! | SenhaForte1! | Erro (E-mail já cadastrado). | - | - |
| alex_valido | Al | alex@email.com | SenhaForte1! | SenhaForte1! | Erro (Nome não atinge limite mínimo). | - | - |
| beto | Beto Carlos | beto@email.com | SenhaForte1! | SenhaForte1! | Erro (Nome de usuário não atinge limite mínimo). | - | - |
| username12345678 | Nome Válido | teste@email.com | SenhaForte1! | SenhaForte1! | Erro (Nome de usuário excedeu limite). | - | - |
| carlos_b | Carlos B. | carlos@email.com | Senha@1 | Senha@1 | Erro (Senha não atinge limite mínimo). | - | - |
| carlos_b | Carlos B. | carlos@email.com | senhafraca1 | senhafraca1 | Erro (Senha fora do padrão exigido). | - | - |
| diana_t | Diana T. | diana@email.com | SenhaForte1! | SenhaForte2@ | Erro (Senhas não coincidem). | - | - |
| Vazio | UI Teste | ui@email.com | SenhaForte1! | SenhaForte1! | Erro (Nome de usuário é obrigatório). | - | - |
| uiteste | Vazio | ui@email.com | SenhaForte1! | SenhaForte1! | Erro (Nome é obrigatório). | - | - |
| uiteste | UI Teste | Vazio | SenhaForte1! | SenhaForte1! | Erro (E-mail é obrigatório). | - | - |
| uiteste | UI Teste | ui@email.com | Vazio | SenhaForte1! | Erro (Senha é obrigatória). | - | - |
| uiteste | UI Teste | ui@email.com | SenhaForte1! | Vazio | Erro (Confirmação obrigatória/Senhas não coincidem). | - | - |

### CDU 008 - Abrir Sessão

#### Fluxo Principal

| Username | Senha | Resultado Esperado | Resultado Obtido | Situação |
| -------- | ----- | ------------------ | ---------------- | -------- |
| usuarioTeste | SenhaForte123! | Autenticação realizada com sucesso e uma nova sessão é iniciada | - | - |
|  | SenhaForte123! | Erro (Campo de username vazio) | - | - |
| usuarioTeste |  | Erro (Campo de senha vazio) | - | - |
|  |  | Erro (Campos de senha e username vazios) | - | - |
