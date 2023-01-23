from web3 import Web3

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
contract = "0x66889816099e6756F4e45b4BAe7CB38d87cC9bEc"

# RPCのURL
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))  # Ganache上のRPC-SERVER
isConnected = web3.isConnected()

# 確認したい対象のウォレットアドレス
accountAddress = "0xcF56Fef51340e28248e1aCd2E574cB47b31EABa4"
privateKey = "a63e75ab6085c987034bfa326614f9e30a57ab925719fca9e999f8a51d2bae13"

if isConnected:
    contract = web3.eth.contract(address=contract, abi=abi)
    # retrieveで現在の値を取得する
    print("初期値:retrieve : {}".format(contract.functions.retrieve().call()))
    # storeを呼び出す
    txn = contract.functions.store(123456789).buildTransaction({
		'gas': 70000,
		'gasPrice': web3.toWei('1', 'gwei'),
		'from': accountAddress,
		'nonce' : web3.eth.getTransactionCount(accountAddress),
	})
    signed_txn = web3.eth.account.signTransaction(txn, private_key=privateKey)
    web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print("変更後:retrieve : {}".format(contract.functions.retrieve().call()))
