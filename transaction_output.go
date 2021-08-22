package main

import "bytes"

//outputs were coins stored
type TXOutput struct {
	Value      int
	PubKeyHash []byte //determines how to unlock output
}

// Lock signs the output
func (out *TXOutput) Lock(address []byte) {
	pubKeyHash := Base58Decode(address)
	pubKeyHash = pubKeyHash[1 : len(pubKeyHash)-4]
	out.PubKeyHash = pubKeyHash
}

//Checks if the output can be used by the owner of the pubkey
//UsesKey method checks that an input uses a specific key to unlock an output
func (out *TXOutput) IsLockedwithKey(pubKeyHash []byte) bool {
	return bytes.Compare(out.PubKeyHash, pubKeyHash) == 0
}

//NewTXOutput creates a new TXOutput
func NewTXOutput(value int, address string) *TXOutput {
	txo := &TXOutput{value, nil}
	txo.Lock([]byte(address))
	return txo
}
