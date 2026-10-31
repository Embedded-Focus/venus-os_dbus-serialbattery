# Vendored third-party code (`dbus-serialbattery/ext/`)

The driver runs on Venus OS devices, where it cannot rely on `pip` being
available or on internet access at install time. For this reason, all
third-party dependencies are vendored into `dbus-serialbattery/ext/` and
shipped inside the release tarball.

## How vendoring works

The script [`ext/update.py`](dbus-serialbattery/ext/update.py) downloads each
package from its upstream source and is the single place where the upstream
origins are defined:

- **Single files** (e.g. `minimalmodbus.py`, `typing_extensions.py`,
  `statistics.py`) are fetched from `raw.githubusercontent.com`.
- **Modules** are extracted from the **latest release tarball** of the
  upstream GitHub repository.

### Supply chain implications

- `update.py` tracks *latest releases*, not pinned versions. When updating
  vendored code, record the resulting version in the table below and mention
  the bump in the changelog, so every shipped version is traceable.
- Downloads are not hash-verified. After updating, review the diff of
  `ext/` before committing.
- The dev/CI dependency set is locked in `uv.lock` (hash-pinned) and audited
  by `uv audit` in CI. Keeping the locked version of a package close to the
  vendored version means CVEs found in the locked set also apply to the
  vendored code. Check the audit results when updating.

## Vendored packages

| Package | Upstream | Version (vendored) | Notes |
|---|---|---|---|
| aenum | [ethanfurman/aenum](https://github.com/ethanfurman/aenum) | 3.1.13 | |
| aiobmsble | [patman15/aiobmsble](https://github.com/patman15/aiobmsble) | unpinned (reads `importlib.metadata`) | |
| aiooui | [Bluetooth-Devices/aiooui](https://github.com/Bluetooth-Devices/aiooui) | 0.1.9 | |
| bleak | [hbldh/bleak](https://github.com/hbldh/bleak) | unknown (no `__version__`) | |
| bleak-retry-connector | [Bluetooth-Devices/bleak-retry-connector](https://github.com/Bluetooth-Devices/bleak-retry-connector) | 4.6.3 | |
| bluetooth-adapters | [Bluetooth-Devices/bluetooth-adapters](https://github.com/Bluetooth-Devices/bluetooth-adapters) | 2.4.0 | |
| minimalmodbus (single file) | [pyhys/minimalmodbus](https://github.com/pyhys/minimalmodbus) | 2.1.1 | patched, see below |
| paho-mqtt | [eclipse-paho/paho.mqtt.python](https://github.com/eclipse-paho/paho.mqtt.python) | 2.1.1 | |
| python-can | [hardbyte/python-can](https://github.com/hardbyte/python-can) | unpinned (reads `importlib.metadata`) | |
| statistics (single file) | [python/cpython `Lib/statistics.py`](https://github.com/python/cpython) | CPython 3.14 branch | backport for older Pythons |
| typing_extensions (single file) | [python/typing_extensions](https://github.com/python/typing_extensions) | tracks `main` | |
| wrapt | [GrahamDumpleton/wrapt](https://github.com/GrahamDumpleton/wrapt) | 2.3.0 | |
| velib_python | [victronenergy/velib_python](https://github.com/victronenergy/velib_python) | tracks latest | Victron Venus OS library |
| dbus-serialbattery_gui-v2 | [mr-manuel/venus-os_dbus-serialbattery_gui-v2](https://github.com/mr-manuel/venus-os_dbus-serialbattery_gui-v2) | tracks latest | GUI integration |
| venus-os_overlay-fs | [mr-manuel/venus-os_overlay-fs](https://github.com/mr-manuel/venus-os_overlay-fs) | tracks latest | service overlay |

## Patched files

Some vendored files carry local patches (e.g. `minimalmodbus.py`, see
references to "patching the vendored ext/minimalmodbus.py" in the driver
code). When updating a patched file, re-apply the patch and verify the
diff against the pristine upstream file.
