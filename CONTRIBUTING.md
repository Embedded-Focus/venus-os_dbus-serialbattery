## Contributing Guidelines

We welcome contributions to dbus-serialbattery! Please follow these steps to help us keep the project organized and high quality:

### How to Contribute

1. **Fork the repository**

   Click the "Fork" button on GitHub and clone your fork locally.

2. **Create a new branch**

   Use a descriptive branch name, e.g. `feature/new-bms-support` or `fix/typo-in-readme`.

3. **Set up the development environment**

   This project uses the [Astral toolchain](https://docs.astral.sh/): [uv](https://docs.astral.sh/uv/) for dependency management, [ruff](https://docs.astral.sh/ruff/) for linting and formatting and [ty](https://docs.astral.sh/ty/) for type checking. A pinned, hash-locked set of dependencies is stored in `uv.lock`.

   ```sh
   # one-time install of uv
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # create the virtual environment and install all locked dependencies
   uv sync --locked

   # run the tests
   uv run pytest
   ```

   > Note: the driver uses velib_python, which is pre-installed on Venus OS devices under
   > `/opt/victronenergy/dbus-systemcalc-py/ext/velib_python`. To use the python files locally,
   > `git clone` the [velib_python](https://github.com/victronenergy/velib_python) project to velib_python and add
   > velib_python to the `PYTHONPATH` environment variable.

4. **Make your changes**

   - Follow the existing code style and structure.
   - Run [ruff](https://docs.astral.sh/ruff/) for formatting and linting: `uv run ruff format .` and `uv run ruff check --fix .`. Ruff is configured in `pyproject.toml` and runs in CI. The [ruff VS Code extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) checks your code on save.
   - Add an entry to the [CHANGELOG.md](https://github.com/mr-manuel/venus-os_dbus-serialbattery/blob/master/CHANGELOG.md) in alphabetical order. Follow the format of existing entries.
   - Add or update documentation if needed.
   - If you add a new BMS, see the [add a new BMS checklist](https://mr-manuel.github.io/venus-os_dbus-serialbattery_docs/general/supported-bms#add-by-opening-a-pull-request).

5. **Test your changes**

   Make sure your code runs without errors at least for 24 hours.

6. **Submit a Pull Request (PR)**

   - Push your branch to your fork and open a PR against the `master` branch.
   - Clearly describe your changes and reference any related issues (e.g. #392).
   - If your PR fixes a bug, include `Fixes #issue_number` in the description.

7. **Respond to feedback**

   - Be ready to make changes if maintainers request them.
   - Keep discussions constructive and focused on the code.

### Code Style

- Formatting and linting are done with [ruff](https://docs.astral.sh/ruff/) (`uv run ruff format .`, `uv run ruff check .`), configuration lives in `pyproject.toml`.
- Type checking is configured with [ty](https://docs.astral.sh/ty/) (`uv run ty check`), but not yet enforced in CI: the existing code base still has diagnostics to fix first (device-only Victron modules like velib_python also cannot be resolved outside a Venus OS device). New code must type-check cleanly.
- Write clear, concise comments and docstrings.

### Supply Chain

- All dependencies are locked in `uv.lock` with hashes. Never install with plain `pip install <package>`. Add the package to `pyproject.toml` (`uv add <package>`) so that it gets locked.
- CI runs `uv sync --locked` (fails if the lockfile is out of date) and `uv audit` on the locked dependencies. Dependabot opens weekly update PRs.
- Third-party code vendored under `dbus-serialbattery/ext/` is documented in [VENDORED.md](VENDORED.md), including the upstream source of each package.
- To generate a hash-pinned `requirements.txt` for environments without uv (e.g. the standalone variant), run:

  ```sh
  uv export --format requirements.txt --hashes --no-dev -o requirements-lock.txt
  ```

### Other Notes

- For major changes, open an issue first to discuss your idea.
- All contributions must be licensed under the project's license.
- Be respectful and collaborative.

Thank you for helping improve dbus-serialbattery!
