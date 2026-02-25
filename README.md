# kwork

[![CI](https://github.com/kesha1225/pykwork/actions/workflows/ci.yml/badge.svg)](https://github.com/kesha1225/pykwork/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/kwork.svg)](https://pypi.org/project/kwork/)
[![Python](https://img.shields.io/pypi/pyversions/kwork.svg)](https://pypi.org/project/kwork/)
[![License](https://img.shields.io/pypi/l/kwork.svg)](LICENSE)
[![Typing](https://img.shields.io/badge/typing-py.typed-informational.svg)](https://peps.python.org/pep-0561/)

Асинхронная, типизированная Python-библиотека для работы с [kwork.ru](https://kwork.ru/) (aiohttp + Pydantic).

## Доверие и ограничения

- Проект **не является официальным** SDK kwork.ru и не аффилирован с площадкой.
- Часть функций работает через **web-endpoint** `kwork.ru` (а не OpenAPI `api.kwork.ru`) и может ломаться без предупреждения.

## Установка

```bash
uv add kwork
```

или последняя версия:

```bash
uv add git+https://github.com/kesha1225/pykwork
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

## Быстрый старт

```python
import asyncio
from kwork import Kwork

async def main() -> None:
    async with Kwork(
        login="login",
        password="password",
        timeout=30.0,
        retry_max_attempts=3,
    ) as api:
        me = await api.get_me()
        print(f"{me.username} | {me.free_amount} {me.currency}")

asyncio.run(main())
```

Ещё примеры см. в `examples/` и в [гайде](docs/guide.md).

## CLI / MCP для AI-агентов

Доступны JSON-first CLI команды и MCP stdio server:

```bash
export KWORK_LOGIN=login
export KWORK_PASSWORD=password

kwork-agent me
kwork-agent dialogs list --page 1
kwork-agent messages send --user-id 123 --text "Hello"
```

Посмотреть все доступные tools (включая auto-exposed методы):

```bash
kwork-agent tools list --include-write
```

Вызвать любой tool напрямую (для полного покрытия):

```bash
kwork-agent call --tool accept_extras --args-json '{"params":{"orderId":123}}'
```

Сгенерировать Markdown-справочник tools:

```bash
kwork-agent tools export-markdown --include-write --output docs/agent-tools.md
```

Готовый файл в репозитории: [docs/agent-tools.md](docs/agent-tools.md)

Запуск MCP-сервера (stdio):

```bash
kwork-agent mcp serve
```

По умолчанию write-tools в MCP отключены. Включить:

```bash
KWORK_MCP_ENABLE_WRITE_TOOLS=1 kwork-agent mcp serve
```

### Docker Compose (MCP stdio)

```bash
cp .env.example .env
docker compose build kwork-mcp
docker compose run --rm -T kwork-mcp
```

`-T` отключает TTY, что обычно лучше для MCP stdio JSON-RPC.

## Документация

- [Главная](docs/index.md)
- [Быстрый старт](docs/getting-started.md)
- [Гайд (подробно)](docs/guide.md)
- [API-справка](docs/api.md)
- [Разработка](docs/development.md)


## Contributors

- [@iamlostshe](https://github.com/iamlostshe)
