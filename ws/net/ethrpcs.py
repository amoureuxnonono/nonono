from web3 import Web3

from ws.chains.ChainIds import (
    ETH,
    HSC,
    BSC,
    BSCTest,
    Polygon,
    PolygonTest,
    Okex,
    OkexTest
)

def get_web3(chainid = BSC):
    if(chainid == ETH):
        return Web3(Web3.HTTPProvider(r'https://rpc.ankr.com/eth'))

    if(chainid == HSC):
        return Web3(Web3.HTTPProvider(r'https://http-mainnet.hoosmartchain.com'))

    if(chainid == BSC):
        return Web3(Web3.HTTPProvider(r'https://bscrpc.com'))

    if(chainid == BSCTest):
        return Web3(Web3.HTTPProvider(r'https://data-seed-prebsc-2-s1.binance.org:8545/'))

    if(chainid == Polygon):
        return Web3(Web3.HTTPProvider(r'https://rpc-mainnet.maticvigil.com/v1/46dc18c937d4ab3b1ce8f544e8ee1fa5e658a2d5'))

    if(chainid == PolygonTest):
        return Web3(Web3.HTTPProvider(r'https://rpc-mumbai.maticvigil.com/v1/46dc18c937d4ab3b1ce8f544e8ee1fa5e658a2d5'))

    if(chainid == Okex):
        return Web3(Web3.HTTPProvider(r'https://exchainrpc.okex.org/'))

    if(chainid == OkexTest):
        return Web3(Web3.HTTPProvider(r'https://exchaintestrpc.okex.org/'))

    return None