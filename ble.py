#!/usr/bin/env python3

import subprocess
import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib

# ===============================
# PARAMÈTRES
# ===============================
BLE_MESSAGE = "GOLDEN-BALISE"   # ≤ ~20 caractères
ADAPTER = "hci0"

# ===============================
# Activation Bluetooth
# ===============================
subprocess.run(
    ["bluetoothctl", "power", "on"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

# ===============================
# DBus / BlueZ
# ===============================
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()

adapter_path = f"/org/bluez/{ADAPTER}"
adapter = bus.get_object("org.bluez", adapter_path)
adapter_props = dbus.Interface(adapter, "org.freedesktop.DBus.Properties")

adapter_props.Set("org.bluez.Adapter1", "Powered", True)

adv_manager = dbus.Interface(
    adapter,
    "org.bluez.LEAdvertisingManager1"
)

# ===============================
# Classe Advertisement (CORRECTE)
# ===============================
class Advertisement(dbus.service.Object):
    PATH = "/org/bluez/example/advertisement0"

    def __init__(self, bus):
        super().__init__(bus, self.PATH)

        self.props = {
            "Type": "peripheral",
            "LocalName": BLE_MESSAGE,
            "Discoverable": True
        }

    @dbus.service.method(
        "org.freedesktop.DBus.Properties",
        in_signature="s",
        out_signature="a{sv}"
    )
    def GetAll(self, interface):
        if interface != "org.bluez.LEAdvertisement1":
            return {}
        return self.props

    @dbus.service.method(
        "org.bluez.LEAdvertisement1",
        in_signature="",
        out_signature=""
    )
    def Release(self):
        print("Advertisement released")


# ===============================
# Lancement
# ===============================
adv = Advertisement(bus)

adv_manager.RegisterAdvertisement(
    adv.PATH,
    {},
    reply_handler=lambda: print("✅ Balise BLE active"),
    error_handler=lambda e: print("❌ Erreur BLE :", e)
)

loop = GLib.MainLoop()
loop.run()
