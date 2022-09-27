from .ChainIds import (
    ETH,
    HSC,
    BSC,
    BSCTest,
    Polygon,
    PolygonTest,
    Okex,
    OkexTest
)

address_dict = { }
  
address_dict[HSC] = '0x78bb0c1ddbab1f7c5ca32b5a0546ec62b377383b'
address_dict[BSCTest] = '0x24dbf1b10aee904c86cf0188093b20b337dc97a8'
address_dict[BSC] = '0x78bb0c1ddbab1f7c5ca32b5a0546ec62b377383b'
address_dict[ETH] = '0x78bb0c1ddbab1f7c5ca32b5a0546ec62b377383b'
address_dict[Polygon] = ''
address_dict[PolygonTest] = '0x010efa39c95b52494172b11ce4b0941cb1d915b4'
address_dict[Okex] = ''
address_dict[OkexTest] = ''

def get_address(chainId):
    return address_dict.get(chainId, '')
