# CLI Task Manager

A command-line task management tool for creating, assigning, prioritizing, filtering, and tracking tasks. Built as a terminal-based alternative to tools like Todoist or Linear, with tasks persisted to a local SQLite database.

## Requirements
 
- Python 3.11+

## Installation

```bash
git clone https://github.com/Damilorlar/personal_budget_tracker_cli
cd project-1-cli-tool
pip install -r requirements.txt
```

## Usage
 
```bash
# Add a task
task add "Write unit tests" --priority high --tag testing --assignee alice
 
# List tasks
task list --assignee alice --status pending
 
# Mark a task as complete
task done 42
 
# Delete a task
task delete 42
```


### Example Output

```
$ task add "Write unit tests" --priority high --tag testing --assignee alice
Task #42 created: "Write unit tests" [HIGH] @alice #testing

$ task list --assignee alice --status pending
┌────┬──────────────────────┬──────────┬──────────┬─────────────┐
│ ID │ Title                │ Priority │ Status   │ Assignee    │
├────┼──────────────────────┼──────────┼──────────┼─────────────┤
│ 42 │ Write unit tests     │ HIGH     │ PENDING  │ alice       │
│ 38 │ Review PR #12        │ MEDIUM   │ PENDING  │ alice       │
└────┴──────────────────────┴──────────┴──────────┴─────────────┘

$ task done 42
Task #42 marked complete.
```

## Architecture

```
CLI Interface (Click / Typer)
        |
Command Handlers (add / list / complete / delete / tag)
        |
Business Logic Layer (Task CRUD, filtering, prioritization)
        |
Storage Layer (SQLite)
```

## Data Model

Each task includes: ID, title, description, status, priority, tags, assignee, and timestamps.

## Development

```bash
# Run tests
pytest

# Run with coverage
pytest --cov
```

### Workflow

1. Create a branch off `main`
2. Commit changes with descriptive messages (e.g. `feat(storage): implement SQLite task persistence`)
3. Open a pull request and assign a reviewer
4. Address feedback and merge


## Team
 
| Role | Name |
| --- | --- |
| Project Lead | |
| CLI Engineer | |
| Storage Engineer | |
| QA / Testing Engineer | |