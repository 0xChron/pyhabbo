# pyhabbo

Unofficial Python SDK for the [Habbo public Web API](https://www.habbo.com/api/public/api-docs/).

> Not affiliated with or endorsed by Sulake Oy or Habbo.

## Install

```bash
pip install pyhabbo
```

Requires **Python 3.11+**.

### Install from source

```bash
git clone https://github.com/0xChron/pyhabbo
cd pyhabbo
pip install -r requirements.txt
pip install .
```

## Quick start

```python
from pyhabbo import HabboClient, Hotel

client = HabboClient(hotel=Hotel.COM)
client.ping()

user = client.users.get_by_name("Habbo")
print(user.name, user.current_level)

profile = client.users.get_profile(user.unique_id)
print(len(profile.badges), len(profile.friends))
```

## Hotels

Pass a `Hotel` to target a specific Habbo hotel:

```python
client = HabboClient(hotel=Hotel.DE)   # habbo.de
client = HabboClient(hotel=Hotel.FI)   # habbo.fi
client = HabboClient(hotel=Hotel.COM)  # habbo.com (default)
```

Available hotels: `COM`, `DE`, `ES`, `FI`, `FR`, `IT`, `NL`, `BR`, `TR`.

You can also pass a custom `base_url` if needed.

## API

### Users

| Method | Endpoint |
|--------|----------|
| `client.users.get_by_name(name)` | `GET /users?name=` |
| `client.users.get(user_id)` | `GET /users/{id}` |
| `client.users.get_profile(user_id)` | `GET /users/{id}/profile` |
| `client.users.list_friends(user_id)` | `GET /users/{id}/friends` |
| `client.users.list_groups(user_id)` | `GET /users/{id}/groups` |
| `client.users.list_rooms(user_id)` | `GET /users/{id}/rooms` |
| `client.users.list_badges(user_id)` | `GET /users/{id}/badges` |

### Achievements

| Method | Endpoint |
|--------|----------|
| `client.achievements.list_all()` | `GET /achievements` |
| `client.achievements.list_for_user(user_id)` | `GET /achievements/{user_id}` |

### Groups

| Method | Endpoint |
|--------|----------|
| `client.groups.get(group_id)` | `GET /groups/{id}` |
| `client.groups.list_members(group_id)` | `GET /groups/{id}/members` |

### Badges

| Method | Endpoint |
|--------|----------|
| `client.badges.get_owners(badge_code)` | `GET /badge/owners/{badgeCode}` |

### Rooms

| Method | Endpoint |
|--------|----------|
| `client.rooms.get(room_id)` | `GET /rooms/{roomId}` |

### Lists

| Method | Endpoint |
|--------|----------|
| `client.lists.list_hotlooks()` | `GET /lists/hotlooks` |

### Marketplace

| Method | Endpoint |
|--------|----------|
| `client.marketplace.batch_stats(room_items=[], wall_items=[])` | `POST /marketplace/stats/batch` |

## Examples

Runnable scripts for each endpoint are in [examples/](examples/).

```bash
git clone https://github.com/0xChron/pyhabbo
cd pyhabbo
pip install .
python examples/public/users/get_by_name.py
```

## Official API docs

[Habbo Web API Swagger UI](https://www.habbo.com/api/public/api-docs/)

## Development

For contributors — clone the repo and install dev dependencies:

```bash
git clone https://github.com/0xChron/pyhabbo
cd pyhabbo
pip install -e ".[dev]"
pytest
ruff check src tests
```

## License

MIT — see [LICENSE](LICENSE).
