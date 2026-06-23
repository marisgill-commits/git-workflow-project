# Contributing Guide — Git Branching Strategy

This project follows **Git Flow**, a professional and widely-used branching model.

## Branch Structure

| Branch | Purpose |
|---|---|
| `main` | Production-ready, stable code only. Never commit directly. |
| `develop` | Integration branch. All finished features merge here first. |
| `feature/<name>` | New feature development (e.g. `feature/multiply`). |
| `hotfix/<name>` | Urgent fixes applied directly on `main`. |

## Workflow Rules

1. Never push directly to `main` or `develop`.
2. Create a new branch from `develop` for every feature:
```bash
   git checkout develop
   git checkout -b feature/<feature-name>
```
3. Commit small, logical changes (see commit convention below).
4. Open a Pull Request (PR) from `feature/<name>` → `develop`.
5. After review, merge and delete the feature branch.
6. When `develop` is stable and tested, merge it into `main` and tag a release:
```bash
   git checkout main
   git merge develop
   git tag -a v1.0.0 -m "Release v1.0.0"
```

## Commit Message Convention (Conventional Commits)

Format: `<type>: <short description>`

| Type | Use case |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `test` | Adding/updating tests |
| `refactor` | Code change that doesn't fix a bug or add a feature |
| `chore` | Maintenance tasks (config, .gitignore, etc.) |

**Examples:**