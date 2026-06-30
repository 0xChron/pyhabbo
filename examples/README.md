# Examples

Sample scripts for each [Habbo public API](https://www.habbo.com/api/public/api-docs/) endpoint.

Install the package first:

```bash
uv sync --extra dev
uv pip install -e .
```

Run any example:

```bash
uv run python examples/public/users/get_by_name.py
```

## Layout

```
examples/public/
├── ping/                    GET /ping
├── users/                   GET /users/...
├── achievements/            GET /achievements/...
├── groups/                  GET /groups/...
├── badge/                   GET /badge/owners/...
├── rooms/                   GET /rooms/...
├── lists/                   GET /lists/...
└── marketplace/             POST /marketplace/stats/batch
```

Paths mirror `/api/public/{folder}/...` on the Habbo API.
