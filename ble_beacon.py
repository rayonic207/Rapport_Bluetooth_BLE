#!/usr/bin/env python3
import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib

BLE_NAME = "GOLDEN_BALISE"
SERVICE_UUID = "9f3c2a10-7b64-4e8d-b1a2-6c5d9e8f4a21"
ADAPTER = "hci0"

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()

adapter_path = f"/org/bluez/{ADAPTER}"
adapter = bus.get_object("org.bluez", adapter_path)
adv_manager = dbus.Interface(adapter, "org.bluez.LEAdvertisingManager1")

class Advertisement(dbus.service.Object):
    PATH_BASE = "/org/bluez/example/advertisement"

    def __init__(self, bus, index):
        self.path = self.PATH_BASE + str(index)
        super().__init__(bus, self.path)

    def get_properties(self):
        return {
            "org.bluez.LEAdvertisement1": {
                "Type": dbus.String("broadcast"),
                "LocalName": dbus.String(BLE_NAME),
                "ServiceUUIDs": dbus.Array([SERVICE_UUID], signature="s"),
                "Includes": dbus.Array(["tx-power"], signature="s"),
            }
        }

    @dbus.service.method("org.freedesktop.DBus.Properties",
                         in_signature="ss", out_signature="v")
    def Get(self, interface, prop):
        return self.get_properties()[interface][prop]

    @dbus.service.method("org.freedesktop.DBus.Properties",
                         in_signature="s", out_signature="a{sv}")
    def GetAll(self, interface):
        return self.get_properties()[interface]

    @dbus.service.method("org.bluez.LEAdvertisement1",
                         in_signature="", out_signature="")
    def Release(self):
        print("Advertisement released")

def main():
    ad = Advertisement(bus, 0)

    adv_manager.RegisterAdvertisement(
        ad.path, {},
        reply_handler=lambda: print("✅ Beacon BLE actif"),
        error_handler=lambda e: print("❌ Erreur BLE :", e)
    )

    GLib.MainLoop().run()

if __name__ == "__main__":
    main()
