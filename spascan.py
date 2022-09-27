from ws import(
    sp_address_scan
)

from ws.kf.pkeys import(
    KeysFactory
)
 
kf = KeysFactory()

start = kf.produce(64)
scancount = 100000000
sp_address_scan(start, scancount, True, -1)