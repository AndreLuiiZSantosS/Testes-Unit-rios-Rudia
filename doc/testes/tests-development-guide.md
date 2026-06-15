# Guia de Padronização de Erros e TDD Incremental em APIs REST com Django REST Framework

Este documento descreve uma estratégia para evoluir uma API REST já existente utilizando:

* **Django**
* **Django REST Framework (DRF)**
* **Testes unitários**
* **Padronização de respostas**
* **TDD incremental**
* **Refatoração orientada a comportamento**

O cenário considerado aqui é:

* Parte da API já foi implementada
* Endpoints já funcionam
* Serializers já possuem validações
* Ainda não existe padronização global de erros
* As respostas podem variar entre endpoints

A proposta é evoluir a API de forma segura e incremental.

---

# Objetivo da estratégia

O objetivo não é “reescrever” a API.

O objetivo é:

```
1. Descobrir o comportamento atual
2. Definir o comportamento desejado através de testes
3. Refatorar gradualmente
4. Introduzir padronização sem quebrar funcionalidades
```

---

# Filosofia adotada

A infraestrutura da API deve surgir como consequência dos testes.

Mesmo em um projeto já existente.

---

# Estratégia correta para APIs já existentes

Quando a API já existe, o fluxo muda um pouco.

Em vez de começar implementando:

```text id="5s4y0d"
implementação → testes
```

Você deve seguir:

```text id="z2k0oe"
comportamento atual
→ testes de caracterização
→ comportamento desejado
→ refatoração
→ padronização
```

---

# O que são testes de caracterização?

São testes que documentam o comportamento atual da API.

Mesmo que o comportamento atual não seja ideal.

Eles servem para:

* evitar regressões
* entender o sistema
* permitir refatoração segura

---

# Exemplo prático

Imagine um endpoint PATCH já existente:

```http id="x5h9ea"
PATCH /users/1/
```

Hoje ele:

* ignora campos inexistentes
* retorna erros inconsistentes
* responde formatos diferentes

Você não deve alterar tudo imediatamente.

Primeiro:

## Capture o comportamento atual em testes

---

# Etapa 1 — Criar testes de caracterização

---

# Exemplo

## Comportamento atual

```python id="w7l9k4"
def test_patch_current_behavior(api_client, user):
    response = api_client.patch(
        f"/users/{user.id}/",
        {
            "unknown_field": "value"
        },
        format="json"
    )

    assert response.status_code == 200
```

Esse teste não representa o comportamento ideal.

Mas documenta o estado atual.

---

# Etapa 2 — Definir o comportamento desejado

Agora você cria novos testes com a nova expectativa arquitetural.

---

# Exemplo

```python id="xal6pz"
def test_patch_should_return_400_for_unknown_field(
    api_client,
    user
):
    response = api_client.patch(
        f"/users/{user.id}/",
        {
            "unknown_field": "value"
        },
        format="json"
    )

    assert response.status_code == 400

    assert response.data["error"]["code"] == (
        "invalid_field"
    )
```

Agora você possui:

* o comportamento atual documentado
* o comportamento desejado definido

---

# Etapa 3 — Refatorar a implementação

Somente agora.

Você altera:

* serializer
* view
* exception handler
* validações

Até satisfazer o novo teste.

---

# Estratégia incremental recomendada

Em APIs já existentes, tente evitar:

* grandes refatorações de uma vez
* padronização global imediata
* mudanças em todos os endpoints simultaneamente

---

# Melhor abordagem

Padronize por camadas.

---

# Ordem recomendada

```text
1. Model tests
2. Serializer tests
3. View tests
4. Error tests
5. Exception handler
```
---

# Testes de Models

Objetivo:

* validar regras de domínio
* validar constraints
* validar métodos internos

---

# Exemplo de testes

## Deve criar usuário válido

```python
def test_should_create_user():
    user = User.objects.create(
        email="test@test.com",
        name="Pedro"
    )

    assert user.id is not None
```

---

## Não deve permitir email duplicado

```python
import pytest
from django.db.utils import IntegrityError

@pytest.mark.django_db
def test_should_not_allow_duplicate_email():
    User.objects.create(
        email="test@test.com",
        name="Pedro"
    )

    with pytest.raises(IntegrityError):
        User.objects.create(
            email="test@test.com",
            name="Outro"
        )
```

---

# O que testar em models

## Regras de domínio

Exemplos:

* cálculo de preço
* status
* geração de slug
* timestamps
* constraints

---

## Não testar

* funcionamento interno do Django ORM
* comportamento nativo do framework

---

# Testes de Serializers

Aqui está uma das partes mais importantes da API.

O serializer define:

* validações
* campos permitidos
* regras de atualização
* comportamento do PATCH/PUT

Em APIs já prontas, o serializer geralmente já contém parte importante das regras.

---

# Casos que DEVEM ter testes

## Payload válido

```python
def test_serializer_should_be_valid():
    serializer = UserSerializer(data={
        "email": "test@test.com",
        "name": "Pedro"
    })

    assert serializer.is_valid()
```

---

## Campo obrigatório ausente

```python
def test_serializer_should_require_email():
    serializer = UserSerializer(data={
        "name": "Pedro"
    })

    assert not serializer.is_valid()
    assert "email" in serializer.errors
```

---

## Campo inválido

```python
def test_serializer_should_validate_email():
    serializer = UserSerializer(data={
        "email": "invalid",
        "name": "Pedro"
    })

    assert not serializer.is_valid()
```

---

## Campo somente leitura

Exemplo importante para PATCH:

```python
def test_serializer_should_not_update_read_only_field(user):
    serializer = UserSerializer(
        user,
        data={"id": 999},
        partial=True
    )

    serializer.is_valid()

    assert "id" not in serializer.validated_data
```

---

# Estratégia ideal para serializers existentes

Você provavelmente já possui:

```python id="jvwhxv"
serializer.is_valid(raise_exception=True)
```

Isso é ótimo.

Porque o DRF já gera exceções padronizáveis.

---

# O que falta então?

Normalmente:

* estrutura global consistente
* códigos de erro
* tratamento uniforme
* comportamento explícito para PATCH

---

# Testes de Views

Aqui você valida:

* status codes
* estrutura da resposta
* autenticação
* autorização
* integração serializer/view

---

# Casos essenciais

| Cenário          | Status esperado |
| ---------------- | --------------- |
| GET sucesso      | 200             |
| POST sucesso     | 201             |
| DELETE sucesso   | 204             |
| Payload inválido | 400             |
| Não autenticado  | 401             |
| Sem permissão    | 403             |
| Não encontrado   | 404             |
| Erro inesperado  | 500             |

---

# Exemplo de teste de criação

```python
def test_should_create_user(api_client):
    response = api_client.post(
        "/users/",
        {
            "email": "test@test.com",
            "name": "Pedro"
        },
        format="json"
    )

    assert response.status_code == 201
```

---

# Exemplo de teste para payload inválido

```python
def test_should_return_400_for_invalid_payload(api_client):
    response = api_client.post(
        "/users/",
        {
            "email": "invalid"
        },
        format="json"
    )

    assert response.status_code == 400

    assert response.data["error"]["code"] == "validation_error"
```

---

# Exemplo — recurso inexistente

```python
def test_patch_should_return_404(api_client):
    response = api_client.patch(
        "/users/999/",
        {
            "name": "Pedro"
        },
        format="json"
    )

    assert response.status_code == 404
```
---

# Problema comum em APIs existentes

Muitas APIs deixam o DRF retornar respostas padrão como:

```json id="v26e4l"
{
  "email": [
    "This field is required."
  ]
}
```

Em outro endpoint:

```json id="2w7q9g"
{
  "detail": "Not found."
}
```

E em outro:

```json id="whpw1t"
{
  "message": "Erro inesperado"
}
```

Isso dificulta:

* frontend
* documentação
* manutenção
* observabilidade

---

# Objetivo da padronização

Transformar tudo em:

```json id="8h3u94"
{
  "error": {
    "code": "validation_error",
    "message": "Erro na requisição",
    "details": {
      "email": [
        "This field is required."
      ]
    }
  }
}
```

---

# Etapa 4 — Criar testes para o formato desejado

---

# Exemplo

```python id="vqql19"
def test_should_return_standardized_validation_error(
    api_client
):
    response = api_client.post(
        "/users/",
        {},
        format="json"
    )

    assert response.status_code == 400

    assert "error" in response.data

    assert response.data["error"]["code"] == (
        "validation_error"
    )
```

---

# Agora sim: implementar o Exception Handler

Somente depois dos testes.

---

# Exemplo de implementação incremental

```python id="3j8z6f"
from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return Response(
            {
                "error": {
                    "code": "internal_error",
                    "message": (
                        "Erro interno do servidor"
                    )
                }
            },
            status=500
        )

    return Response(
        {
            "error": {
                "code": "api_error",
                "message": "Erro na requisição",
                "details": response.data
            }
        },
        status=response.status_code
    )
```

---

# Registrar no settings.py

```python id="s6q8im"
REST_FRAMEWORK = {
    "EXCEPTION_HANDLER":
        "core.exceptions.custom_exception_handler"
}
```

---

# Evolução segura do handler global

Não tente resolver tudo imediatamente.

Primeiro:

## Apenas padronize o envelope da resposta

---

# Depois evolua

Adicione:

* códigos específicos
* tradução de mensagens
* tratamento por tipo de exceção
* logging
* correlation ids
* observabilidade

---

# Exemplo de evolução gradual

---

## Fase 1

```json id="jlwmxt"
{
  "error": {
    "code": "api_error"
  }
}
```

---

## Fase 2

```json id="ojhfb5"
{
  "error": {
    "code": "validation_error"
  }
}
```

---

## Fase 3

```json id="fwb4d3"
{
  "error": {
    "code": "invalid_field",
    "details": {
      "email": [
        "Formato inválido"
      ]
    }
  }
}
```
---

# Testes importantes para APIs já existentes

---

# Serializers

| Caso               | Deve testar |
| ------------------ | ----------- |
| campo obrigatório  | ✔           |
| formato inválido   | ✔           |
| read_only          | ✔           |
| partial update     | ✔           |
| campo desconhecido | ✔           |

---

# Views

| Caso         | Deve testar |
| ------------ | ----------- |
| sucesso      | ✔           |
| validação    | ✔           |
| not found    | ✔           |
| autenticação | ✔           |
| permissão    | ✔           |

---

# Error handling

| Caso             | Deve testar |
| ---------------- | ----------- |
| formato padrão   | ✔           |
| erro interno     | ✔           |
| validation error | ✔           |
| 404              | ✔           |

---

# O que NÃO fazer em APIs existentes

---

# Não refatore tudo ao mesmo tempo

Evite:

```text id="6l7c4u"
“Vamos padronizar todos os endpoints agora”
```

Isso costuma gerar regressões.

---

# Não remover comportamento sem testes

Primeiro capture.

Depois altere.

---

# Não espalhar try/except pelas views

Centralize no handler global.

---

# Não misturar responsabilidades

| Camada            | Responsabilidade |
| ----------------- | ---------------- |
| Model             | domínio          |
| Serializer        | validação        |
| View              | fluxo HTTP       |
| Exception handler | padronização     |

---

# Estratégia profissional recomendada

O fluxo ideal para sua situação é:

```text id="87tzq8"
1. Mapear comportamento atual
2. Criar testes de caracterização
3. Definir comportamento desejado
4. Criar novos testes
5. Refatorar serializers
6. Introduzir handler global
7. Padronizar respostas
8. Refinar arquitetura
```

---

# Resultado esperado

Ao final, você terá:

* API evoluindo sem regressões
* comportamento documentado por testes
* infraestrutura guiada por contratos
* padronização consistente
* base semelhante a APIs profissionais maduras
