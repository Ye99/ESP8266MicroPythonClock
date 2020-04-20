# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import uos
# Make machine available in repl
import machine
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc

import webrepl
webrepl.start()

gc.collect()


def reload(mod):
    import sys
    z = __import__(mod)
    del z
    del sys.modules[mod]
    return __import__(mod)

