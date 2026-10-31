# dbus-serialbattery

This driver is for Venus OS devices (any GX device sold by Victron or a Raspberry Pi running the Venus OS image).

The driver will communicate with a Battery Management System (BMS) that support serial (RS232, RS485 or TTL UART) and Bluetooth communication (see [BMS feature comparison](https://mr-manuel.github.io/venus-os_dbus-serialbattery_docs/general/features#bms-feature-comparison) for details). The data is then published to the Venus OS system (dbus). The main purpose is to act as a Battery Monitor in your GX and supply State of Charge (SoC) and other values to the inverter/charger.

## History

The first version of this driver was released by [Louisvdw](https://github.com/Louisvdw/dbus-serialbattery) in September 2020.

In February 2023 I ([mr-manuel](https://github.com/mr-manuel)) made my first PR, since Louis did not have time anymore to contribute to this project.

With the release of `v1.0.0` I became the main developer of this project. From then on, I have been maintaining the project and developing it further. I'm also solving 99% of the issues on GitHub.

A big thanks to [Louisvdw](https://github.com/Louisvdw/dbus-serialbattery) for the initiation of this project.

## Support this project

This project takes a lot of time and effort to maintain, answering support requests, adding new features and so on.
If you are using this driver and you are happy with it, please make a donation to support me and this project.

[<img src="https://github.md0.eu/uploads/donate-button.svg" height="38">](https://www.paypal.com/donate/?hosted_button_id=3NEVZBDM5KABW)

## Documentation

* [Introduction](https://mr-manuel.github.io/venus-os_dbus-serialbattery_docs/)
* [Features](https://mr-manuel.github.io/venus-os_dbus-serialbattery_docs/general/features)
* [Supported BMS](https://mr-manuel.github.io/venus-os_dbus-serialbattery_docs/general/supported-bms)
* [How to connect and prepare the battery/BMS](https://mr-manuel.github.io/venus-os_dbus-serialbattery_docs/general/connect)
* [How to install, update, disable, enable and uninstall](https://mr-manuel.github.io/venus-os_dbus-serialbattery_docs/general/install)
* [How to troubleshoot](https://mr-manuel.github.io/venus-os_dbus-serialbattery_docs/troubleshoot/)
* [FAQ](https://mr-manuel.github.io/venus-os_dbus-serialbattery_docs/faq/)

### Developer Remarks

To develop this project, install the requirements. This project makes use of velib_python which is pre-installed on
Venus-OS Devices under `/opt/victronenergy/dbus-systemcalc-py/ext/velib_python`. To use the python files locally,
`git clone` the [velib_python](https://github.com/victronenergy/velib_python) project to velib_python and add
velib_python to the `PYTHONPATH` environment variable.

Make sure that the GitHub Actions can run in your repository. Select in your repository settings under `Actions` -> `General` -> `Actions permissions` the option `Allow all actions and reusable workflows`. The workflows declare the permissions that they need, so you can keep the default workflow permissions. The checks run ruff (linting and formatting), a dependency audit (`uv audit`), CodeQL, and the test suite. See [CONTRIBUTING.md](CONTRIBUTING.md) on how to set up the development environment with uv.

See this checklist, if you want to [add a new BMS](https://mr-manuel.github.io/venus-os_dbus-serialbattery_docs/general/supported-bms#add-by-opening-a-pull-request)

#### How it works

* Each supported BMS needs to implement the abstract base class `Battery` from `battery.py`.
* `dbus-serialbattery.py` tries to figure out the correct connected BMS by looping through all known implementations of `Battery` and executing its `test_connection()`. If this returns true, `dbus-serialbattery.py` sticks with this battery and then periodically executes `dbushelpert.publish_battery()`. `publish_battery()` executes `Battery.refresh_data()` which updates the fields of Battery. It then publishes those fields to dbus using `dbushelper.publish_dbus()`
* The Victron Device will be "controlled" by the values published on `/Info/` - namely:
  * `/Info/MaxChargeCurrent `
  * `/Info/MaxDischargeCurrent`
  * `/Info/MaxChargeVoltage`
  * `/Info/BatteryLowVoltage`
  * `/Info/ChargeRequest` (not implemented in dbus-serialbattery)

For more details on the Victron dbus interface see [the official victron dbus documentation](https://github.com/victronenergy/venus/wiki/dbus)

## Try it out — no setup required!

Curious what dbus-serialbattery looks and feels like in action? Explore the interactive demo and play around with all the settings — completely risk-free. Nothing is saved, nothing can go wrong, and no device is needed. It's a great way to get familiar with the interface before or during your own setup.

[Launch the interactive demo](https://mr-manuel.github.io/venus-os_gui-v2/)

## Join the community on Discord

https://discord.gg/YXzFB8rSgx

## Help translating to your language

Are you using this driver and you would like to have it in your language? Now you can help to translate it on [POEditor](https://poeditor.com/join/project/sA2DhyEpYh).
