# 🚀 Guia de Instalação e Execução - Backend (Rudia)

Este guia detalha o passo a passo para configurar, instalar e executar o backend do projeto Rudia.

## 🛠️ 1. Pré-requisitos

Antes de iniciar, certifique-se de ter as seguintes tecnologias instaladas no seu sistema:

- **Git**: Para clonar o repositório.
- **Python (3.10+)**: A linguagem base do projeto.
- **PostgreSQL**: O banco de dados utilizado.

> [!NOTE]
> Para instalar essas ferramentas no Ubuntu/Debian:
> ```bash
> sudo apt update
> sudo apt install git python3 python3-venv postgresql postgresql-contrib
> ```

## 📥 2. Clonar o Repositório

Clone o repositório do projeto na sua máquina local e acesse o diretório principal:

```bash
git clone <URL_DO_REPOSITORIO>
cd Rudia
```

## 🐍 3. Criar e Ativar o Ambiente Virtual

Recomenda-se criar um ambiente virtual para isolar as dependências do projeto.

No diretório raiz do projeto, execute:

```bash
# Criação do ambiente virtual
python3 -m venv venv

# Ativação do ambiente virtual (Linux/macOS)
source venv/bin/activate

# Ativação do ambiente virtual (Windows)
venv\Scripts\activate
```

## 📦 4. Instalar Dependências

Com o ambiente virtual ativado, navegue até a pasta do backend e instale as dependências listadas no arquivo `requirements.txt`:

```bash
cd pds-distribuido/backend
pip install -r requirements.txt
```

## 🗄️ 5. Configurar o Banco de Dados PostgreSQL

O projeto espera um banco de dados PostgreSQL rodando localmente. Conforme estabelecido no `settings.py`, as credenciais e configurações padrões são:
- **Nome do banco**: `rudia`
- **Usuário**: `postgres`
- **Senha**: `postgres`
- **Host**: `localhost` (porta `5432`)

Para configurar rapidamente este banco e usuário com as credenciais padrão, você pode abrir o terminal do PostgreSQL (como o usuário `postgres` do sistema):

```bash
sudo -u postgres psql
```

E então executar os seguintes comandos SQL:

```sql
ALTER USER postgres WITH PASSWORD 'postgres';
CREATE DATABASE rudia OWNER postgres;
\q
```

## ⚙️ 6. Criar e Configurar o Arquivo `.env`

O projeto utiliza variáveis de ambiente listadas num arquivo de exemplo em `.env-example`.

Estando no diretório `pds-distribuido/backend`, você precisa criar um arquivo `.env` nesta pasta copiando o modelo de exemplo:

```bash
cp ../../.env-example/.env-example .env
```

> [!IMPORTANT]
> O arquivo `.env` contém configurações sensíveis, como chave secreta (`SECRET_KEY`), modo de depuração (`DEBUG`), bem como acesso ao banco de dados. Este fluxo garante que as variáveis que o seu `settings.py` precisa estarão à sua disposição.

## 🏗️ 7. Executar Migrações

No diretório do backend (`pds-distribuido/backend`), utilize primeiro o script de preparação `.sh` feito para rodar o comando `makemigrations` em todos os aplicativos do projeto, gerando os esquemas do BD:

```bash
# Dê permissão de execução ao script (apenas Linux/macOS)
chmod +x migrations.sh

# Execute o script para gerar os arquivos de migração
./migrations.sh
```

Atenção: O script acima apenas prepara os arquivos de migração. O próximo passo é aplicar efetivamente essas migrações recém-criadas no seu banco de dados rodando:

```bash
python manage.py migrate
```

## 🧪 8. (Opcional) Carregar Dados de Uso (Mock)

Para facilitar os testes com a API REST que está sendo desenvolvida, você pode popular as tabelas do banco de dados com informações pré-prontas contidas em `mock.json`.

É um passo altamente recomendado durante o desenvolvimento:

```bash
python manage.py loaddata mock.json
```

## 🚀 9. Executar o Servidor

Agora que tudo está configurado, as dependências instaladas e o banco de dados pronto, basta inicializar o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

Após rodar o comando, a aplicação estará acessível em sua máquina local sob a URL padrão `http://127.0.0.1:8000/`.

> [!WARNING]
> Lembre-se que sempre que for rodar a aplicação novamente, o **ambiente virtual Python deve ser ativado** e o serviço do **PostgreSQL deve estar ligado** (normalmente fica ativo em segundo plano nativamente na maioria das instalações Linux/macOS/Windows).
