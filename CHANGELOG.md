# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-06-30

### Added

- `HabboClient` with multi-hotel support via `Hotel` enum
- Users API: lookup by name/id, profile, friends, groups, rooms, badges
- Achievements API: catalog and per-user achievements
- Groups API: group details and members
- Badges API: badge owner counts
- Rooms API: room details by ID
- Lists API: hot looks (XML response parsing)
- Marketplace API: batch stats (POST)
- Pydantic models for all supported endpoints
- Custom exceptions: `HabboAPIError`, `NotFoundError`, `BadRequestError`
- Runnable examples under `examples/public/`
- CI workflow (pytest + ruff on Python 3.11–3.13)

[Unreleased]: https://github.com/0xChron/pyhabbo/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/0xChron/pyhabbo/releases/tag/v0.1.0
