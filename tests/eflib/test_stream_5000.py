from custom_components.ef_ble.eflib import NewDevice
from custom_components.ef_ble.eflib.devicebase import DeviceBase
from custom_components.ef_ble.eflib.devices.stream_5000 import Device


def test_stream_5000_is_discovered(mocker):
    ble_dev = mocker.Mock()
    ble_dev.address = "AA:BB:CC:DD:EE:FF"
    adv_data = mocker.Mock()
    adv_data.manufacturer_data = {
        DeviceBase.MANUFACTURER_KEY: b"\x00ES21XXXXXXXXXXXX"
    }

    device = NewDevice(ble_dev, adv_data)

    assert isinstance(device, Device)
    assert device.serial_number == "ES21XXXXXXXXXXXX"
