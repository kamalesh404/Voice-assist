# Contributing to Aura

First off, thank you for considering contributing to Aura. It's people like you that make Aura such a powerful and extensible Voice Assistant for everyone.

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** the forked repository to your local machine.
3. **Install** the dependencies using `make setup`.
4. **Create a branch** for your feature or bug fix: `git checkout -b feature/your-feature-name`.

## Development Guidelines

- **Code Style:** We enforce strict PEP-8 compliance. Please run `make lint` before submitting a PR.
- **Testing:** All new features must include unit tests in the `tests/` directory. Run `make test` to ensure everything passes.
- **Plugins:** If you are adding a new automation skill, please place it in the `plugins/` directory and follow the standard plugin interface.

## Submitting a Pull Request

- Ensure your commit messages are descriptive.
- Push your branch to your fork and submit a PR against our `main` branch.
- A project maintainer will review your code and may request changes.
