# Быстрый старт

## Установка

Рекомендуемый способ (через `uv`):

```bash
uv add kwork
```

Альтернатива (pip):

```bash
pip install kwork
```

Если нужен socks5-прокси:

```bash
pip install "kwork[proxy]"
```

Если нужен MCP-сервер для AI-агентов:

```bash
pip install "kwork[mcp]"
```

## Подключение и контекстный менеджер

Клиент держит сессию и авторизацию, поэтому удобнее работать через `async with`:

```python
import asyncio
from kwork import Kwork


async def main() -> None:
    async with Kwork(login="login", password="password") as api:
        me = await api.get_me()
        print(me.username)


asyncio.run(main())
```

## Таймауты и ретраи

В конструкторе можно настроить таймауты и повторные попытки (429/5xx и сетевые ошибки):

```python
from kwork import Kwork

api = Kwork(
    login="login",
    password="password",
    timeout=30.0,
    retry_max_attempts=3,
    retry_backoff_base=0.5,
    retry_backoff_max=8.0,
    retry_jitter=0.1,
    relogin_on_auth_error=True,
)
```

## Частые операции

### Получить собственный профиль

```python
me = await api.get_me()
```

### Список проектов (биржа)

```python
projects = await api.get_projects(
    categories_ids=[11, 79],
    price_from=1000,
    price_to=50000,
    hiring_from=50,
    page=1,
)
```

### Web-login (куки для `kwork.ru`)

```python
await api.web_login(url_to_redirect="/exchange")
```

Дальше можно выполнять web-действия через `api.web`, например отклик на проект. Детали: [гайд](guide.md).

## CLI / MCP (для агентов)

CLI возвращает JSON и подходит для автоматизации:

```bash
export KWORK_LOGIN=login
export KWORK_PASSWORD=password

kwork-agent me
kwork-agent user get --user-id 123
kwork-agent dialogs list --all
```

Полный список tools (включая auto-exposed методы `KworkClient` и `KworkWebClient`):

```bash
kwork-agent tools list --include-write
```

Универсальный вызов любого tool:

```bash
kwork-agent call --tool get_user_info --args-json '{"params":{"id":123}}'
```

Сгенерировать Markdown-справочник tools:

```bash
kwork-agent tools export-markdown --include-write --output docs/agent-tools.md
```

См. также: [agent-tools.md](agent-tools.md)

MCP stdio server:

```bash
kwork-agent mcp serve
```

В MCP-режиме write tools по умолчанию отключены. Для включения:

```bash
KWORK_MCP_ENABLE_WRITE_TOOLS=1 kwork-agent mcp serve
```

### Docker Compose (stdio MCP server)

```bash
cp .env.example .env
docker compose build kwork-mcp
docker compose run --rm -T kwork-mcp
```
