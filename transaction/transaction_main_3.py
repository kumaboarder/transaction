from web3 import Web3

# 確認したい対象のウォレットアドレス
myWalletAddress = "0x00xx"

# RPCのURL
web3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com")) 
isConnected = web3.isConnected()

# ABI
abi = '''
[
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "num",
				"type": "uint256"
			}
		],
		"name": "store",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "retrieve",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
'''
# コントラクトアドレス
contract = "0xd9145CCE52D386f254917e481eB44e9943F39138"

if isConnected:
    contract = web3.eth.contract(address=contract, abi=abi)
    print(contract.functions.name().call())
    print(contract.functions.symbol().call())

    balance = contract.functions.balanceOf(myWalletAddress).call()
    print(web3.fromWei(balance, 'ether'))