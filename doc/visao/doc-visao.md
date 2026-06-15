# Documento de Visão

## Histórico de Revisões

| Data                | Versão              | Descrição           | Autores                                  |
| :-----------------: | :-----------------: | :-----------------: | :--------------------------------------: |
| 26/04/2025          | 1.0                 | Versão inicial      |  João Vitor Bezerra e Pedro Lucas Xavier |
| 31/05/2025          | 2.0                 | Atualizando RFs e Usuários     |  João Vitor Bezerra |
| 21/09/2025          | 3.0                 | Revisão do Documento           |  João Vitor Bezerra, Mateus Miranda e Gabriel Henrique |

<br>

## Sumário

### [1. 🎯 Objetivo do Projeto](#1--objetivo-do-projeto-1)
### [2. 📝 Descrição do Problema](#2--descrição-do-problema-1)
### [3. 👥 Descrição dos Usuários](#3--descrição-dos-usuários-1)
### [4. 🏠 Descrição do Ambiente dos Usuários](#4--descrição-do-ambiente-dos-usuários-1)
### [5. 🔑 Principais Necessidades dos Usuários](#5--principais-necessidades-dos-usuários-1)
### [6. ⚔️ Alternativas Concorrentes](#6-️-alternativas-concorrentes-1)
### [7. 🌐 Visão Geral do Produto](#7--visão-geral-do-produto-1)
### [8. ✅ Requisitos Funcionais (RF)](#8--requisitos-funcionais)
### [9. 📌 Requisitos Não Funcionais (RNF)](#9--requisitos-não-funcionais)
### [10. ⚙️ Tecnologias do Projeto ](#11-️-tecnologias-do-projeto-1)

<br>

## 1. 🎯 Objetivo do projeto

O Rudiá é um roteirizador de viagens turísticas, o qual abrange toda a área do Rio Grande do Norte. Seu objetivo é fornecer um guia virtual para facilitar a tarefa de construir um roteiro, considerando pontos como, por exemplo, transporte, hospedagem, restaurantes e pontos turísticos. A aplicação visa a usabilidade descomplicada, tornando fácil uma tarefa díficil.

<br>

## 2. 📝 Descrição do problema

|     |     |
| --- | --- |
| **Problema**            | Ausência de soluções que proporcionem unidade, autonomia, segurança e organização no planejamento de viagens no estado do Rio Grande do Norte. |
| **Afeta**               | São afetados por esse problema o setor do turismo norte riograndense (turistas, empreendedores e trabalhadores do setor) e, consequentemente, a economia local. |  
| **Impacta**             | Espera-se um aumento na busca por destinos turísticos no estado do Rio Grande do Norte, não somente entre os mais conhecidos e divulgados, mas também entre locais pouco explorados e visitados. |
| **Solução**             | Desenvolver uma aplicação que possibilite ao viajante planejar sua viajem de forma fácil e rápida, fornecendo dicas e sugestões que enriqueçam sua experiência turística, além de conectá-lo a outros viajantes, promovendo o compartilhamento de experiências, engajamento e conexão. |

<br>

## 3. 👥 Descrição dos usuários 

| Nome                |  Descrição          | Responsabilidade    |
| -----------------   | -----------------   | -----------------   |
| Visitante | Usuário de acesso primário à aplicação | Acesso limitado à aplicação podendo visualizar o feed com as principais postagens da comunidade, acessar o catálogo de descobertas de atrações para viagem e realizar buscas pelas informações sobre os serviços das etapas do roteiro de viagem e, também, criar um **Roteiro Rápido** sem a opção de salvamento |
| Rudiero | Usuário do sistema que possui um perfil de **Rudiero** | Acesso completo à parte da aplicação para usuários padrão podendo visualizar o feed com as postagens da comunidade e interagir com outros usuários publicando ou comentando nas postagens, visualizar o catálogo de descobertas de atrações para as viagens, realizar a busca das informações sobre os serviços das etapas do roteiro de viagem e criar **Roteiros Rápidos** e **Roteiros Personalizados** ao seu gosto com a opção de salvamento. Além disso, também podem realizar uma avaliação completa dos serviços e dos roteiros de viagem |
| Parceiro | Usuário do sistema que possui um perfil de **Parceiro** | Acesso completo à parte da aplicação para usuários parceiro podendo visualizar e interagir no feed da comunidade com outros usuários, além de realizar o cadastro de seus estabelecimentos ou seus serviços para serem visualizados na aplicação pelos **Rudieros** e, também, possuir acesso as postagens e avaliações dos **Rudieros** sobre seus estabelecimentos e seus serviços |
| Moderador | Usuário do sistema com privilégios administrativos restritos | **Agente de Controle de Qualidade e Conformidade** que está responsável por analisa e validar as propostas de parceria e serviço, além de avaliar e resolver as denuncias registradas na plataforma. Além disso, podendo também interagir com outros usuários por meio de comentarios nas postagens do feed da aplicação |
| Administrador | Usuário que administra as partes da aplicação | Responsável por gerenciar os perfis de usuarios (**Rudieros**, **Parceiros** e **Moderadores**), os serviços dos **Parceiros**, as publicações do feed da comunidade e seus comentários, as tags de serviços e as categorias que as tags são relacionadas. |

<br>

## 4. 🏠 Descrição do ambiente dos usuários

### Ambiente dos Rudieros

Ao iniciar uma sessão como **Rudieiro**, o usuário acessa o seu ambiente virtual. A tela inicial oferece informações curadas especificamente para ele, baseadas em páginas que ele segue, em seus favoritos, em sua localização e outros fatores. De maneiro geral, o Rudiero pode utilizar a principal ferramenta da aplicação (a criação de roteiros) e outras funcionalidades, como a interação com a comunidade, edição de perfil, pesquisa de serviços e gerenciamento dos seus roteiros. Todo esse ambiente deve ser apresentado de maneira simples e intuitiva, visando o uso descomplicado, de acordo com objetivo do projeto.

### Ambiente dos Parceiros

O login feito com as credenciais de um **Parceiro** traz uma apresentação de dados diferente dos usuários viajantes. A página inicial mostra, em destaque, os serviços geridos por esse Parceiro, apenas com informações resumidas, mas permitindo o acesso a uma página detalhada para cada item. Logo abaixo, um feed exibe os posts relacionados aos seus serviços e também as publicações das páginas seguidas pelo usuário. Numa sessão de Parceiro, as principais funcionalidades disponíveis são o gerenciamento dos serviços oferecidos, a edição dos dados públicos e privados, a publicação de postagens e comentários ligados aos serviços e o cadastro de novas opções ao público. Essas ferramentas mostram-se em uma interface de uso simples e prático, não exigindo nenhum conhecimento técnico específico do usuário.

### Ambiente dos Moderadores

A área dos **Moderadores** oferece acesso, principalmente, às solicitações de novos parceiros e serviços, permitindo que esse usuário analise o perfil das solicitações e envie uma resposta. Além disso, o moderador também poderá visualizar e resolver as denúncias feitas dentro da aplicação; essa funcionalidade acarreta em outro aspecto do ambiente dos moderadores: eles podem visualizar todo o conteúdo da comunidade - roteiros, postagens, comentários, perfis, entre outros -, mas não podem interagir como usuários-padrão, comentando ou reagindo. Isso garante que esse tipo de usuário consiga performar o seu trabalho de análise de denúncias, mas sem interações desnecessárias.

<br>

## 5. 🔑 Principais necessidades dos usuários

Os **Rudieros** desejam uma aplicação prática e rápida para o planejamento de sua viagem a qual disponibilize da criação de roteiros que unifiquem todos os serviços das etapas de elaboração da viagem de maneira personalizada por meio de filtros que seguem as suas preferências. Também é esperado a possibilidade de compartilhar suas experiências e seus roteiros e interagir com a comunidade da Rudiá.

Os **Parceiros** buscam uma aplicação que possua a funcionalidade de divulgação para seus serviços e que disponha das análises de acesso, comentários, avaliações e publicações que envolvam esses serviços. Além disso, buscam ampliar o seu público com uma alternativa inovadora que busca cativar com a criação de roteiros completos com diversas combinações do serviço prestado com as demais etapas da viagem e também possibilitar uma maior interação com o seu público - os Rudieros.

Os **Moderadores** necessitam de um sistema que possibilite a fácil visualização das solicitações de parceria, serviço e denúncias, usufruindo de uma área intuitiva para a resolução desses pedidos. Ademais, pede-se uma visualização livre dos dados públicos que envolvam as funções de análise já citadas, a fim de permitir o exercício da tarefa de moderação.

<br>

## 6. ⚔️ Alternativas concorrentes

**Booking.com**, **Trip.com**, **Hoteis.com**, **Expedia** - conecta o turista ao prestador de serviço (hospedagem, voos, aluguel de carros, etc.), utilizando a infraestrutura do site para fechar as reservas dos serviços e tratar as demais questões relacionadas (cancelamento, reembolso, etc.). Funciona como um marketplace de viagens. Também possibilita ao usuário fazer um comparativo de preços dos serviços desejados e aos prestadores de serviço a possibilidade de colocar o seu serviço em evidência frente a outros serviços, por meio de anúncios pagos.

**Airbnb** - Semelhante às alternativas acima na função de reservar estadias, mas diferencia-se na natureza das hospedagens: os chamados anfitriões são pessoas físicas que disponibilizam locais para hospedagem. Ademais oferece as mesmas funcionalidades já citadas acima, como pagamento pela plataforma, cancelamento, reembolso e avaliação do usuário.

**Tripadvisor** - planejador de viagens que conecta o usuário a outros viajantes, promovendo o compartilhamento de experiências de viagens. Também possibilita ao usuário descobrir opções de lazer, gastronomia, excursões, etc. no local desejado. Os usuários podem avaliar os serviços contratados e compartilhar fotos e comentários sobre suas experiências.

**Trivago** - mecanismo de metabusca que compara preços e ofertas de acomodações fornecidos por vários sites de reservas no mundo todo, incluindo agências de viagens online, redes de hotéis e acomodações independentes. O usuário utiliza o trivago para comparar preços dos serviços e realiza a reserva no site de sua preferência.

<br>

## 7. 🌐 Visão geral do produt

A **Rudiá** possui uma proposta inovadora que busca como principal objetivo a praticidade e a rapidez na elaboração de roteiros de viagem personalizados para cada usuário, sendo a unificação de serviços de todas as etapas de uma viagem realizadas em uma única aplicação. A Rudiá também propõe um ambiente interativo entre os usuários (**Rudieros** e **Parceiros**) disponibilizando através de um sistema de mídia social o compartilhamento das aventuras turísticas no Rio Grande do Norte de maneira singular por cada usuário. A Rudiá destaca-se por sair dos padrões de aplicativos de turismo que abordam cada etapa da viagem de maneira singular, disponibilizando informações de hospedagem, transporte, lazer, alimentação e turismo em todo o Rio Grande do Norte em uma só aplicação.

Além disso, a Rudiá também inclui as parcerias com pequenos, médios e grandes empreendedores, disponibilizando uma plataforma de divulgação de serviços e possibilitando uma interatividade direta entre os prestadores de serviços e os clientes no sistema de mídia social da Rudiá. A aplicação também disponibiliza as análises de acesso, os comentários, as avaliações e as publicações feitas pelos Rudieros fornecendo uma total dimensão do engajamento do serviço em todo RN. A inovadora ideia de roteirização completa da viagem também enaltece os serviços dos Parceiros que possuem combinações diversas com todas as etapas da viagem.

<br>

## 8. ✅ Requisitos funcionais

| Legenda | Prioridade | Dificuldade |
|---------|------------|-------------|
| 🔴      | Alta       | Alta        |
| 🟡      | Media      | Media       |
| 🟢      | Baixa      | Baixa       |

<br>

| Código              | Nome                | Descrição           | Prioridade          | Dificuldade | Ator |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: | :---------: | :--: |
| RF01 | **Realizar Auto Cadastro de Rudiero** | Permitir o **Visitante** realizar o auto cadastro fornencendo os dados pessoais e criando um  **Username** e **Senha** para obter acesso ao **perfil de Rudiero** na aplicação | 🟡 | 🟢 | Visitante |
| RF02 | **Submeter Proposta de Parceria** | Permitir o **Visitante** realizar a submissão do formulário de proposta de parceria fornencendo os dados do empreendedor ou empresa, criando um  **Username** e **Senha** e submetendo o serviço para divulgação (**RF03**) para serem analisados pelo **Moderador** (**RF20**) e assim obter acesso ao **perfil de Parceiro** na aplicação | 🟡 | 🟡 | Visitante |
| RF03 | **Submeter Proposta de Serviço** | Permitir o **Visitante** (**RF02**) ou o **Parceiro** realizar a submissão do formúlario de proposta de serviço fornencendo os dados do serviço e adicionando **Tags**. A proposta passará pela analise do **Moderador** (**RF21**) para ser divulgado na aplicação | 🟡 | 🟡 | Visitante e Parceiro |
| RF04 | **Realizar Login** | Permitir os usuários (**Rudieros** e **Parceiros**) abrirem uma sessão fornecendo **Username** e **Senha** para acessarem o seu perfil na aplicação com permissões condizentes ao tipo da conta | 🟡 | 🟢 | Rudiero e Parceiro |
| RF05 | **Personalizar Perfil** | Permitir os usuários (**Rudiero** e **Parceiro**), após abrirem uma sessão, gerenciarem seus dados visiveis ou não para outros usuários. **Rudiero** as preferencias das informações na aplicação e seus roteiros, **Parceiro** gerenciar os dados da empresa ou empreendedor e os serviços. E ambos os usuários as publicações realizadas. | 🟢 | 🔴 | Rudiero e Parceiro  |
| RF06 | **Criar Roteiro Rápido** | Permitir o **Visitante** ou **Rudiero** criar roteiros rápidos por meio de perguntas pré-estabelecidas sobre os serviços e informações das etapas da viagem e fornecendo com base nas respostas 3 possibilidades de roteiros prontos para o uso com a possibilidade de salvamento apenas para o **Rudiero** | 🟡 | 🔴 | Visitante e Rudiero |
| RF07 | **Criar Roteiro Personalizado** | Permitir o **Rudiero** analisar e escolher com base nas suas preferencias os serviços e informações sobre cada etapa da viagem elaborando de maneira autoral seu próprio roteiro | 🔴 | 🟡 | Rudiero |
| RF08 | **Filtrar e Ordenar** | Permitir os usuários (**Visitante**, **Rudiero** e **Parceiro**) filtrarem e organizarem as informações fornecidas na aplicação por meio da barra de filtragem | 🟢 | 🟡 | Visitante, Rudiero e Parceiro |
| RF09 | **Criar Postagens e Realizar Comentarios** | Permitir o **Rudiero** compartilhar fotos, serviços e roteiros com a comunidade. Também permitir que o **Parceiro** divulgue seus serviços por meio de postagens e ambos, **Rudiero** e **Parceiro**, e os **Moderadores** possam interagir por meio de comentários nas postagens | 🟢 | 🔴 | Rudiero, Parceiro e Moderador |
| RF10 | **Realizar Denuncia** | Permitir os usuários (**Rudiero** e **Parceiro**) realizarem denuncias sobre perfis, serviços, publicações e comentários que possuem conteúdo nocivo segundo as diretrizes da aplicação | 🟢 | 🟡 | Rudiero e Parceiro |
| RF11 | **Realizar Busca Avançada** | Permitir o **Rudiero** buscar novas localidades e serviços por meio de uma página de busca simplificada contendo fotos com pequenas descrições | 🟢 | 🟢 | Rudiero |
| RF12 | **Realizar Avaliação** | Permitir o **Rudiero** avaliar a experiência de seus roteiros de maneira singular (cada serviço) ou completa (roteiro completo) | 🟡 | 🟡 | Rudiero |
| RF13 | **Analisar Denúncias** | Permitir o **Moderador** analisar as denúncias dos usuários (**Rudiero** e **Parceiro**) em relação a perfis, serviços, publicações e comentários | 🟢 | 🟡 | Moderador |
| RF14 | **Analisar Proposta de Parceria** | Permitir o **Moderador** analisar os dados das propostas enviadas pelos **Visitantes** para permitir a persistência de um perfil de **Parceiro** | 🟡 | 🟢 | Moderador |
| RF15 | **Analisar Proposta de Serviço** | Permitir o **Moderador** analisar os dados das propostas enviadas pelos **Visitantes** (**RF02**) e/ou **Parceiros** para permitir a persistência do serviço na aplicação | 🟡 | 🟢 | Moderador |
| RF16 | **Gerenciar Aplicação** | Permitir o **Administrador** realizar o gerenciamento das partes criticas da aplicação como perfis de usuários, serviços dos **Parceiros**, publicações e seus comentarios e tags e as categorias que estão vinculadas | 🟡 | 🟢 | Administrador |

<br>

## 9. 📌 Requisitos não-funcionais

| Legenda | Classificação |
|---------|---------------|
| 🟥      | Obrigatório   |
| 🟩      | Opcional      |

| Código              |  Nome               |  Descrição          |  Categoria          |  Classificação      |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| RNF01 | **Criptografia de Dados** | Os dados sensíveis dos usuários na aplicação devem ser criptografados | Segurança | 🟥 |
| RNF02 | **Lei de Proteção de Dados (LPD)** | Os dados fornecidos pelos usuários devem está conforme a LPD | Segurança | 🟥 |
| RNF03 | **Responsividade da Aplicação** | A aplicação deve ter capacidade de interação com dispositivos moveis | Compatibilidade | 🟥 |
| RNF04 | **Autenticação e Permissões** | Criação de sessões para salvamento de dados de perfil dos usuários, permitindo-os acessar os seus perfis com suas devidas permissões | Segurança | 🟥 |
| RNF05 | **Modo Offline** | Permitir o **Rudiero** obter informações específicas do roteiro de viagem sem a necessidade de conexão a internet | Compatibilidade | 🟩 |

<br>

## 10. ⚙️ Tecnologias do Projeto

### **Frontend**

[![Tecnologias Frontend](https://skillicons.dev/icons?i=next,react,tailwind&perline=3)](https://skillicons.dev)

### **Backend**

[![Tecnologias Backend](https://skillicons.dev/icons?i=django&perline=1)](https://skillicons.dev)

### **Banco de Dados**

[![Tecnologias Banco de Dados](https://skillicons.dev/icons?i=postgres&perline=1)](https://skillicons.dev)

### **Controle de Versão**

[![Tecnologias Banco de Dados](https://skillicons.dev/icons?i=git,github&perline=2)](https://skillicons.dev)