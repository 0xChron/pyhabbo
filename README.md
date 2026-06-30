# pyhabbo

Unofficial Python SDK for the [Habbo public Web API](https://www.habbo.com/api/public/api-docs/).

See [examples/](examples/) for runnable example scripts per endpoint.

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Setup

```bash
git clone https://github.com/0xChron/pyhabbo
cd pyhabbo

# Create venv and install dependencies
uv sync --extra dev

# Install the package in editable mode
uv pip install -e .
```

## Commands

```bash
# Run the test suite
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Lint
uv run ruff check src tests

# Format
uv run ruff format src tests

# Quick manual smoke test against the live API
uv run python -c "from pyhabbo import HabboClient; c = HabboClient(); c.ping(); c.close(); print('ping OK')"
```

## Usage

```python
from pyhabbo import HabboClient, Hotel

client = HabboClient(hotel=Hotel.COM)
client.ping()

user = client.users.get_by_name("Habbo")
print(user.name, user.current_level)

profile = client.users.get_profile(user.unique_id)
print(len(profile.badges), len(profile.friends))
```


Use a different hotel by passing `hotel=Hotel.DE` (or `.FI`, `.FR`, etc.). You can also pass a custom `base_url` if needed.



### Users API

| Method | Endpoint |
|--------|----------|
| `client.users.get_by_name(name)` | `GET /users?name=` |
| `client.users.get(user_id)` | `GET /users/{id}` |
| `client.users.get_profile(user_id)` | `GET /users/{id}/profile` |
| `client.users.list_friends(user_id)` | `GET /users/{id}/friends` |
| `client.users.list_groups(user_id)` | `GET /users/{id}/groups` |
| `client.users.list_rooms(user_id)` | `GET /users/{id}/rooms` |
| `client.users.list_badges(user_id)` | `GET /users/{id}/badges` |

### Achievements API

| Method | Endpoint |
|--------|----------|
| `client.achievements.list_all()` | `GET /achievements` |
| `client.achievements.list_for_user(user_id)` | `GET /achievements/{user_id}` |

### Groups API

| Method | Endpoint |
|--------|----------|
| `client.groups.get(group_id)` | `GET /groups/{id}` |
| `client.groups.list_members(group_id)` | `GET /groups/{id}/members` |

### Badges API

| Method | Endpoint |
|--------|----------|
| `client.badges.get_owners(badge_code)` | `GET /badge/owners/{badgeCode}` |

### Rooms API

| Method | Endpoint |
|--------|----------|
| `client.rooms.get(room_id)` | `GET /rooms/{roomId}` |

### Lists API

| Method | Endpoint |
|--------|----------|
| `client.lists.list_hotlooks()` | `GET /lists/hotlooks` (XML) |

### Marketplace API

| Method | Endpoint |
|--------|----------|
| `client.marketplace.batch_stats(room_items=[], wall_items=[])` | `POST /marketplace/stats/batch` |


## API reference

Official docs: [Habbo Web API Swagger UI](https://www.habbo.com/api/public/api-docs/)

## License

MIT - See [LICENSE](LICENSE)
