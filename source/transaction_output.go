package main

import (
	"bytes"
	"encoding/gob"
	"log"
)

//outputs were coins stored
type TXOutput struct {
	Value      float32
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
func NewTXOutput(value float32, address string) *TXOutput {
	txo := &TXOutput{value, nil}
	txo.Lock([]byte(address))
	return txo
}

//TXOutputs collects TXOutput
type TXOutputs struct {
	Outputs []TXOutput
}

//Seralise seralises TXOuputs
func (outs TXOutputs) Serialize() []byte {
	var buff bytes.Buffer

	enc := gob.NewEncoder(&buff)
	err := enc.Encode(outs)
	if err != nil {
		log.Panic(err)
	}

	return buff.Bytes()
}

// DeserializeOutputs deserializes TXOutputs
func DeserializeOutputs(data []byte) TXOutputs {
	var outputs TXOutputs

	dec := gob.NewDecoder(bytes.NewReader(data))
	err := dec.Decode(&outputs)
	if err != nil {
		log.Panic(err)
		//log.Fatal("Failed Deserializing")
	}

	return outputs
}
