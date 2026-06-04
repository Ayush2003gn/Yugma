# Yukta v1.0.0

A modular task management application built in Python.

Yukta provides a structured task management workflow using pages, priorities, status tracking, and persistent storage while maintaining a clean layered architecture for future expansion.

---

# Features

## Task Management

- Add tasks
- Remove tasks
- Update tasks
- Mark tasks as done
- Mark tasks as undone
- Change task priority
- Task tracking with timestamps

## Page Management

- Create pages
- Remove pages
- Set default page
- Category-based organization

## Display System

- Display all tasks
- Display by day
- Display by week
- Display by month
- Display by year
- Completion analysis

## Persistent Storage

- JSON-based storage
- Automatic data loading
- Automatic data saving
- Manifest-based page tracking

---

# Identification System

Every task contains two identifiers.

## User ID (UID)

Human-friendly identifier used by users.

Example:

```text
Y1
Y2
Y3
```

Used in:

```bash
remove -uid Y1
update -uid Y2
done -uid Y3
```

---

## Internal ID (IID)

Unique internal identifier used by the application.

Example:

```text
550e8400-e29b-41d4-a716-446655440000
```

Used internally for:
- business logic
- storage
- task tracking

---

# Architecture

```text
User
 ↓
CLI
 ↓
Parser
 ↓
Action Layer
 ↓
Models
 ↓
Storage Layer
 ↓
Renderer
```

---

# Project Structure

```text
core/
├── action/
├── contracts/
├── models/
├── renderer/
├── storage/
├── ui/
└── utils/

tests/
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/<your-username>/Yukta.git
cd Yukta
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

# Testing

Run all tests:

```bash
pytest
```

---

# Command Categories

## Task Commands

```text
add
remove
update
done
undone
priority
```

## Page Commands

```text
page
```

## Display Commands

```text
display
analysis
```

## Utility Commands

```text
help
exit
```

---

# Version 1.0.0

Initial stable release.

Highlights:

- Modular parser architecture
- Layered application design
- UID/IID task identification system
- Page-based task organization
- JSON persistence system
- Comprehensive command validation
- Integration and model testing

---

# Roadmap

Future versions may include:

- Terminal User Interface (TUI)
- SQLite backend
- GUI support
- Web interface
- Advanced analytics

---

# License

MIT License