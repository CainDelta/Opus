package main

import "fmt"

func main() {
	bc := NewBlockChain()
	bc.AddBlock("Send 1 BTC to Mbx")
	bc.AddBlock("Send 10 BTC to N")

	for _, block := range bc.blocks {
		fmt.Printf("Prev. hash: %x\n", block.PrevBlockHash)
		fmt.Printf("Data: %s\n", block.Data)
		fmt.Printf("Hash: %x\n", block.Hash)
		fmt.Println()
	}

}
