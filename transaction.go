package main

import (
	"bytes"
	"crypto/sha256"
	"encoding/gob"
	"encoding/hex"
	"fmt"
	"log"
)

const subsidy = 10

type Transaction struct {
	ID   []byte
	Vin  []TXInput
	Vout []TXOutput
}

//outputs indivisible , spent as a whole
//outputs were coins stored
type TXOutput struct {
	Value        int
	ScriptPubKey string //determines how to unlock output
}

//references output
type TXInput struct {
	Txid      []byte
	Vout      int
	ScriptSig string
}

func NewCoinBaseTX(to, data string) *Transaction {
	if data == "" {
		fmt.Sprintf("Reward to '%s'", to)
	}
	//initial coinbase trans, - empty txid, no value ie -1 and data is just string
	txin := TXInput{[]byte{}, -1, data}
	txout := TXOutput{subsidy, to} //subsidy is the amount of reward, scriptkey is to address
	tx := Transaction{nil, []TXInput{txin}, []TXOutput{txout}}
	tx.SetID()
	return &tx
}

// SetID sets ID of a transaction
func (tx *Transaction) SetID() {
	var encoded bytes.Buffer
	var hash [32]byte

	enc := gob.NewEncoder(&encoded)
	err := enc.Encode(tx)
	if err != nil {
		log.Panic(err)
	}
	hash = sha256.Sum256(encoded.Bytes())
	tx.ID = hash[:]
}

// CanUnlockOutputWith checks whether the address initiated the transaction
func (in *TXInput) CanUnlockOutputWith(unlockingData string) bool {
	return in.ScriptSig == unlockingData
}

// CanBeUnlockedWith checks if the output can be unlocked with the provided data
func (out *TXOutput) CanBeUnlockedWith(unlockingData string) bool {
	return out.ScriptPubKey == unlockingData
}

func (bc *Blockchain) FindUnspentTransactions(address string) []Transaction {

	var unspentTXs []Transaction
	spentTXOs := make(map[string][]int)
	bci := bc.Iterator()

	for {
		block := bci.Next()

		for _, tx := range block.Transactions {
			txID := hex.EncodeToString(tx.ID)

		Outputs:
			for outIdx, out := range tx.Vout {
				//Was the output spent ?
				//check if output referneced in an input
				if spentTXOs[txID] != nil {
					for _, spentOut := range spentTXOs[txID] {
						if spentOut == outIdx {
							continue Outputs
						}
					}
				}
				//get outputs that can be unlocked with the address and append to unspent
				if out.CanBeUnlockedWith(address) {
					unspentTXs = append(unspentTXs, *tx)
				}
			}
			if tx.IsCoinbase() == false {
				for _, in := range tx.Vin {
					if in.CanUnlockOutputWith(address) {
						inTxID := hex.EncodeToString(in.Txid)
						spentTXOs[inTxID] = append(spentTXOs[inTxID], in.Vout)
					}
				}
			}

		}

		if len(block.PrevBlockHash) == 0 {
			break
		}

		//The function returns a list of transactions containing unspent outputs.
	}

	return unspentTXs

}
