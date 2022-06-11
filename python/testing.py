from hashlib import sha256|
import hashlib



x = 5
y = 0 # We don't know what y should be yet...
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1
print(f'The solution is y = {y}')y

sha256(5)
sha256(f'{x*y}'.encode()).hexdigest()

def proof_of_work(last_proof):
    """
    Simple Proof of Work Algorithm:
     - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
     - p is the previous proof, and p' is the new proof
    :param last_proof: <int>
    :return: <int>
    """

    proof = 0
    while valid_proof(last_proof, proof) is False:
        proof += 1

    return proof


def valid_proof(last_proof, proof):
    """
    Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
    :param last_proof: <int> Previous Proof
    :param proof: <int> Current Proof
    :return: <bool> True if correct, False if not.
    """

    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"


proof_of_work(100)

curl -X POST -H "Content-Type: application/json" -d '{
 "nodes":["http://127.0.0.1:5001"]
}' "http://localhost:5000/nodes/register"



####GOLANG TESTING
import subprocess
import os
import random
import time
#subprocess.run(["ls"]).read()



https://mega.nz/folder/LYRlXQ7D#1zm2IxWnlwCS45v5a3Nj3w/folder/WMAEmB7S

######## 3001 CREATE WALLETS  #######################
env = {
    **os.environ,
    "NODE_ID": str(3001),
}

os.getcwd()
#subprocess.Popen('/usr/bin/mybinary', env=env).wait()

for i in range(200):
    subprocess.Popen("blockchain_go.exe createwallet",env=env, shell=True, stdout=subprocess.PIPE).stdout.read().splitlines()

################### 3000 ###############33

import subprocess
import os
import random
import time




###SEED FUNCTION
def seed():
    """Function seeds 10 random addresses with coin to kickstart process """
    env = {
        **os.environ,
        "NODE_ID": str(3001),
    }
    wallets = subprocess.Popen("blockchain_go listaddresses",env=env, shell=True, stdout=subprocess.PIPE).stdout.read().splitlines()
    wallets = [x.decode("utf-8") for x in wallets]

    ###Switch to master node
    env = {**os.environ,
        "NODE_ID": str(3000)}

    master_wallet = '1DG899e57P4SCrVv3UkUpwp5Uh8H3PrHBS'
    for x in range(10):
        #addr = random.choice(wallets)
        balance_text = 'blockchain_go getbalance -address ' + master_wallet
        balance = subprocess.Popen(balance_text, shell=True,env=env, stdout=subprocess.PIPE).stdout.read().splitlines()[0].decode("utf-8")
        amount = float(balance.split(':')[1].strip())
        if amount <= 0.0:
            pass
        else:
            sendto = random.choice(wallets)
            send_amount = random.uniform(0.01,amount/2)
            print(sendto,'--',send_amount)
            send = 'blockchain_go send -from '+master_wallet+' -to ' + sendto + ' -amount ' + str(send_amount) +  ' -mine'
            subprocess.Popen(send, shell=True,env=env, stdout=subprocess.PIPE).stdout.read().splitlines()
            time.sleep(5)

seed()


env = {
    **os.environ,
    "NODE_ID": str(3001),
}



def listbalances():
    wallets = subprocess.Popen("blockchain_go listaddresses",env=env, shell=True, stdout=subprocess.PIPE).stdout.read().splitlines()
    wallets = [x.decode("utf-8") for x in wallets]
    for i in wallets:
        balance_text = 'blockchain_go getbalance -address ' + i
        balance = subprocess.Popen(balance_text, shell=True,env=env, stdout=subprocess.PIPE).stdout.read().splitlines()[0].decode("utf-8")
        amount = float(balance.split(':')[1].strip())
        print(i,'---',amount)


####NODE 3001 needs to be synced up to master node alternatively just copy genesis node to blockchain_3001
listbalances()


wallets = subprocess.Popen("blockchain_go listaddresses",env=env, shell=True, stdout=subprocess.PIPE).stdout.read().splitlines()
wallets = [x.decode("utf-8") for x in wallets]
##For loop goes through wallets, checks balance of address, if above zero sends to random in wallet if not passses
for x in range(6000):
    addr = random.choice(wallets)
    balance_text = 'blockchain_go getbalance -address ' + addr
    balance = subprocess.Popen(balance_text, shell=True,env=env, stdout=subprocess.PIPE).stdout.read().splitlines()[0].decode("utf-8")
    amount = float(balance.split(':')[1].strip())
    ##print(addr,'---',amount)
    if amount <= 0.0:
        pass
    else:
        sendto = random.choice(wallets)
        send_amount = random.uniform(0.01,amount)
        send = 'blockchain_go send -from '+addr+' -to ' + sendto + ' -amount ' + str(send_amount)
        subprocess.Popen(send, shell=True,env=env, stdout=subprocess.PIPE).stdout.read().splitlines()
        time.sleep(12)







for x in sendlist:
    amount = random.uniform(1,10)
    send = 'blockchain_go send -from 1EkBaqgkFTQpeGni5fkWp7sjCAMsawVmWP -to ' + x + ' -amount ' + str(amount)
    subprocess.Popen(send, shell=True,env=env, stdout=subprocess.PIPE).stdout.read().splitlines()
    time.sleep(10)


subprocess.Popen('blockchain_go send -from 171Wup33u3hVYp79kcEAyMEWcwSwPuT1b8 -to 1QJidz1cHUcPBNdCUN3UAgdabk1xoAanpC', shell=True, stdout=subprocess.PIPE).stdout.read().splitlines()


subprocess.Popen(['blockchain_go.exe'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()




##############PROCESS BLOCKCHAIN ###############
import pandas as pd
import json
import shortuuid
import numpy as np

with open('blockchain3000.json','r') as f:
    data = json.loads(f.read())

#pd.concat([blocks[['BlockHash']].reset_index(drop=True),masters_trans],axis=1)


s = 'kunatira'
s.split('')
n = 0
for i in list(s):
    n+=1
    print(n)


####TRANSACTIONS SECTION
trans = pd.json_normalize(data,record_path=['Transactions']).explode('Vout').explode('Vin')
transactions_blocks = pd.concat([pd.json_normalize(data).explode('Transactions')[['BlockHash']].reset_index(drop=True),pd.json_normalize(data,record_path=['Transactions'])[['ID']]],axis=1)
Vin = pd.json_normalize(trans['Vin']) #use pd.io.json
Vout = pd.json_normalize(trans['Vout'])
Transactions = pd.concat([Vin.reset_index(drop=True), Vout], axis=1)
masters_trans  = pd.concat([trans[['ID']].reset_index(drop=True),Transactions],axis=1)
masters_trans['TransactionID'] = masters_trans['ID']
masters_trans['ID'] =  np.arange(masters_trans.shape[0])
masters_trans.to_csv('master_trans.csv',index=False)
transactions_blocks.to_csv('transactions_blocks.csv',index=False)
transactions_blocks



mas
####BLOCKS
blocks = pd.json_normalize(data)
blocks.to_csv('blocks.csv',index=False)
masters_trans[masters_trans['ID']==2]
masters_trans.TransactionID.unique()
