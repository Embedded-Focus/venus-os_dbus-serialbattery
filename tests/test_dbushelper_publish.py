"""Regression tests for DbusHelper.publish_battery()."""

from unittest.mock import MagicMock

from pytest import MonkeyPatch

import dbushelper


def _publish_helper_for_battery(battery: MagicMock) -> dbushelper.DbusHelper:
    helper = dbushelper.DbusHelper.__new__(dbushelper.DbusHelper)
    helper.battery = battery
    helper.error = {"cleared": True, "count": 0, "timestamp_first": None, "timestamp_last": None}
    helper.cell_voltages_good = None
    helper.bms_cable_alarm = 0
    helper.disconnect_threshold = 999
    helper._dbusname = "com.victronenergy.battery.vecan1__0x01"
    helper.publish_dbus = MagicMock()
    helper.telemetry_upload = MagicMock()
    return helper


def _connected_battery_with_temperatures() -> MagicMock:
    battery = MagicMock()
    battery.refresh_data.return_value = True
    battery.temperature_1 = 10.0
    battery.temperature_2 = 20.0
    battery.temperature_3 = 30.0
    battery.temperature_4 = 40.0
    battery.temperature_mos = None
    battery.online = False
    battery.state = 9
    battery.error_code_last_reset_check = 0
    battery.connection_info = None
    battery.get_allow_to_charge.return_value = True
    battery.get_allow_to_discharge.return_value = True
    return battery


def test_publish_battery_keeps_missing_mos_temperature_as_none(monkeypatch: MonkeyPatch) -> None:
    battery = _connected_battery_with_temperatures()
    helper = _publish_helper_for_battery(battery)
    loop = MagicMock()

    monkeypatch.setattr(dbushelper.utils, "TEMPERATURE_1_ADJUST", [1.0, 2.0])
    monkeypatch.setattr(dbushelper.utils, "TEMPERATURE_2_ADJUST", [0.0, 1.0])
    monkeypatch.setattr(dbushelper.utils, "TEMPERATURE_3_ADJUST", [0.0, 1.0])
    monkeypatch.setattr(dbushelper.utils, "TEMPERATURE_4_ADJUST", [0.0, 1.0])
    monkeypatch.setattr(dbushelper.utils, "TEMPERATURE_MOS_ADJUST", [1.0, 2.0])

    helper.publish_battery(loop)

    # publish_battery catches exceptions and quits the loop, so this is the
    # observable failure signal for the original TypeError.
    loop.quit.assert_not_called()
    assert battery.temperature_1 == 21.0
    assert battery.temperature_mos is None
    helper.publish_dbus.assert_called_once()
