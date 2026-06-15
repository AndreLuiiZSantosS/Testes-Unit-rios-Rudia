# 🚀 Guia de Instalação e Execução - Frontend (Rudia)

Este guia detalha o passo a passo para configurar, instalar e executar a aplicação frontend do projeto Rudia (feita em Next.js).

## 🛠️ 1. Pré-requisitos

Antes de iniciar, certifique-se de ter as seguintes tecnologias instaladas no seu sistema:

- **Git**: Para clonar o repositório.
- **Node.js**: Ambiente de execução necessário (recomendamos a versão **18.17+** ou superior).
- **pnpm**: O gerenciador de pacotes adotado para este projeto frontend.

> [!NOTE]
> Se você já possui o Node.js mas não tem o `pnpm`, pode instalá-lo globalmente no seu sistema executando:
> ```bash
> npm install -g pnpm
> ```

## 📥 2. Clonar o Repositório

Caso ainda não o tenha feito, clone o repositório do projeto na sua máquina local e acesse o diretório principal:

```bash
git clone <URL_DO_REPOSITORIO>
cd Rudia
```

## 📦 3. Instalar Dependências

Navegue até a pasta do frontend e utilize o `pnpm` para baixar e construir as dependências listas do projeto:

```bash
cd pds-distribuido/frontend
pnpm install
```

> [!TIP]
> Foi escolhido o uso do `pnpm` na aplicação por sua grande eficiência e velocidade. Ele lerá o arquivo `pnpm-lock.yaml` garantindo exata paridade das dependências para todo o time.

## ⚙️ 4. (Opcional) Configurar o Arquivo de Variáveis de Ambiente

Neste projeto frontend específico, caso necessite estipular portas diferentes e URLs de API, crie um arquivo `.env` (ou `.env.local`) dentro da raiz do `/frontend`.

> [!IMPORTANT]
> O seu arquivo `next.config.ts` já se encontra estruturado por padrão para aceitar integração com imagens e comunicação para o backend Django rodando em `127.0.0.1:8000` / `localhost:8000`. Não é necessário configuração adicional de variáveis para o desenvolvimento local básico se o backend obedeceu o formato de sua porta padrão.

## 🚀 5. Executar o Servidor

Agora que todas as dependências estão devidamente instaladas, você pode inicializar o servidor de desenvolvimento do Next.js:

```bash
pnpm dev
```

Por trás dos panos, o projeto foi configurado para iniciar o serviço de forma otimizada com o **Turbopack** (`next dev --turbopack`), acelerando substancialmente o tempo de build em ambiente de desenvolvimento.

Dentro de instantes, a aplicação base estará disponível, geralmente em `http://localhost:3000/` (verifique a porta exata sugerida pelo Next no seu terminal).

> [!WARNING]
> Para o total funcionamento dinâmico da aplicação, lembre-se de que o **servidor Backend do Django e o PostgreSQL** também deverão estar sendo executados num terminal separado conforme orientado no guia de backend!
