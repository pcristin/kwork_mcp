from __future__ import annotations

import sys

from kwork.agent.cli import main as cli_main
from kwork.agent.cli import main_mcp as cli_main_mcp


def main() -> None:
    raise SystemExit(cli_main())


def main_mcp() -> None:
    raise SystemExit(cli_main_mcp(sys.argv[1:]))


if __name__ == "__main__":
    main()
