# Changelog

## v1.0.0

### Added(core)

- Task management system
- Page management system
- UID/IID architecture
- Display filters
- JSON storage
- Parser contracts
- Action layer
- Renderer layer
- Test suite

### Notes(v1.0.0)

- First stable release.

## v1.0.1

### Fixed(storage)

- Fixed storage loading issue where tasks were not restored after application restart.
- Fixed duplicate page creation during storage import.
- Improved storage initialization reliability.

### Result(v1.0.1)

- Tasks now persist correctly across application restarts.

## v1.0.2(branding)

### Fixed (storage)

- Yugma stores application data in: %APPDATA%\Yugma\

- Structure:
Yugma/
├── data/
│   ├── manifest.json
│   └── *_data.json
│
└── logs/
    └──*.log

### Result (v1.0.2)

- Tasks now persist correctly across application restarts.