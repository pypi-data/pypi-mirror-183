# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 17:05:59 2022

bluetooth_tx_example.py

python-can-bluetooth
"""

import can
from can import Message
from threading import Timer
from time import ctime

from ..can_bluetooth import BluetoothSPPBus


DONE = False

# with can.Bus(interface="bluetooth", channel="COM5", bitrate=250000, echo=False) as bus:
with BluetoothSPPBus(channel="COM5", bitrate=250000, echo=False) as bus:

    def timeout():
        global DONE
        DONE = True

    msg = Message(
        arbitration_id=0xC0FFEF,
        is_extended_id=True,
        data=[0xDE, 0xAD, 0xBE, 0xEF, 0xDE, 0xAD, 0xBE, 0xEF],
    )

    task = bus.send_periodic(msg, 1)
    t = Timer(10, timeout)
    t.start()
    print(f"TX started: {ctime()}")

    while not DONE:
        pass
    else:
        task.stop()
        print(f"TX Done: {ctime()}")
