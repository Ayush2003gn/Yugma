# Yukta

Yukta is a modular command-line productivity system built with Python.

The project focuses on:
- clean architecture
- modularity
- predictable execution flow
- task management
- long-term scalability

Current version: `v0.1.0`

---

# Features

## Task Management
- create tasks
- remove tasks
- mark tasks as done/undone
- set task priority

## Category System
- create multiple task pages/categories
- set default category
- category-based task filtering

## Display System
- display all tasks
- display by:
  - year
  - month
  - week
  - day
- analysis mode with completion bars

## Persistence
- automatic JSON storage
- automatic import/export system

## Debugging & Logging
- centralized logging system
- debug log file generation

## Architecture
- modular layered structure
- separated storage/business/CLI logic

---

# Project Structure

```text
Yukta/
│
├── core/
│   ├── logger.py
│   ├── manager.py
│   ├── storage.py
│   │
│   └── models/
│       ├── task.py
│       ├── tasklist.py
│       └── taskpage.py
│
├── data/
│   └── *.json
│
├── debug/
│   └── app.log
│
├── tests/
│
├── main.py
├── pytest.ini
├── README.md
└── LICENSE
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Ayush2003gn/Yukta.git
cd Yukta
```

## Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate:

### Windows
```bash
venv\Scripts\activate
```

### Linux / Mac
```bash
source venv/bin/activate
```

---

# Run Project

```bash
python main.py
```

---

# Command Guide

# Page Commands

## Create Category
```bash
page add study
```

## Create and Set Default
```bash
page add study --sd
```

## Set Default Category
```bash
page set-default study
```

## Remove Category
```bash
page remove study
```

---

# Task Commands

## Add Task
```bash
add -t "Complete chemistry notes"
```

## Add Task to Specific Category
```bash
add -t "Solve maths problems" --C study
```

## Add Task with Priority
```bash
add -t "Prepare for exam" --P high
```

## Add Task and Mark Done
```bash
add -t "Drink water" --MD
```

---

# Delete Commands

## Remove Task
```bash
delete -id <task_id>
```

---

# Status Commands

## Mark Done
```bash
status -id <task_id> --MD
```

## Mark Undone
```bash
status -id <task_id> --MUD
```

---

# Display Commands

## Display All Tasks
```bash
display
```

## Display All with Category
```bash
display --all --C study
```

## Display Analysis
```bash
display --analysis
```

## Display by Year
```bash
display --year 2026
```

## Display by Month
```bash
display --month May 2026
```

## Display by Week
```bash
display --week 20 2026
```

## Display by Day
```bash
display --day 11 5 2026
```

---

# Testing

Run tests using pytest:

```bash
pytest
```

---

# Current Limitations

- argument parsing is still improving
- no GUI/TUI yet
- UI IDs reset after restart
- command validation is still evolving

---

# Development Goals

## Near Future
- safer parser system
- stronger pytest coverage
- command refactoring
- update/edit task system

## Long Term
- TUI/GUI
- reminder system
- scheduling
- analytics dashboard
- plugin architecture

---

# Philosophy

Yukta is designed as a system-first productivity application.

The goal is not only task management, but also learning:
- software architecture
- modular design
- scalable systems
- debugging discipline
- clean execution flow

---

# License

This project is licensed under the MIT License.