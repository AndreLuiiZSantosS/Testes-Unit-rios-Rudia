---
description: "Use when writing Django/DRF unit tests, TDD incremental, or standardizing API error responses. Covers TestCase choices, test naming, and error envelope expectations."
applyTo: "**/tests/**/*.py, **/test_*.py"
---
# Django/DRF unit tests + API error standardization

- Prefer TDD incremental for existing endpoints: write characterization tests first, then desired behavior tests, then refactor.
- Avoid large refactors or global error changes without tests; standardize errors gradually by layer.
- Follow the recommended order: model tests, serializer tests, view tests, error tests, then exception handler.

## Base classes

- Use `django.test.TestCase` for tests that need the database.
- Use `rest_framework.test.APITestCase` for API endpoint tests (DRF).
- Use `unittest.TestCase` only for pure logic that does not touch the database.

## API tests

- Always use `self.client` for requests; validate with `self.assertEqual(response.status_code, ...)` and `response.data`.
- For PATCH behavior, include tests for unknown fields, read-only fields, and partial updates.

## Data setup

- Prefer `setUpTestData(cls)` for shared fixtures across methods.
- Use `setUp(self)` only when data must be reset per test.

## Mocks

- Use `unittest.mock.patch` to isolate external services or network calls.

## Authentication

- Whenever a test requires authentication, create the user within `setUpTestData` or utilize a `UserFactory`.
- Prefer using `self.client.force_authenticate(user=self.user)` for unit and view integration tests to avoid the overhead of generating real tokens for every test execution.
- For every protected endpoint, it is mandatory to implement tests covering:
   - **401 Unauthorized:** Requests sent without a token or user session.
   - **403 Forbidden:** Authenticated users who lack permission to interact with that specific resource.

## Naming + structure

- Test file names must start with `test_`.
- Test method names: `test_should_[result]_when_[condition]`.
- Follow AAA with comments:
  - `# Arrange` (setup)
  - `# Act` (execute)
  - `# Assert` (verify)

## Error response expectations

- Prefer standardized error envelopes in new tests, for example:
  - `response.data["error"]["code"] == "validation_error"`
  - `response.data["error"]["details"]` for validation fields
- Introduce a global exception handler only after tests define the desired envelope.

Full error envelope example:

```json
{
  "error": {
    "code": "validation_error",
    "message": "Erro na requisicao",
    "details": {
      "email": [
        "This field is required."
      ]
    }
  }
}
```

Note: consult the guide at [../../doc/testes/tests-development-guide.md](../../doc/testes/tests-development-guide.md).
