from web3 import Web3

# 確認したい対象のウォレットアドレス
myWalletAddress = "0x0000xx"

# RPCのURL
web3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com")) 
isConnected = web3.isConnected()

if isConnected:
    print('Connected')
    balance_wei = web3.eth.getBalance(myWalletAddress)
    print(web3.fromWei(balance_wei,'ether'))
else:
    print('Cant connect.')