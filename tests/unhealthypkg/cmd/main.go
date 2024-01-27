package main

import "log"

type BaldGuy struct {
	Name      string
	HairCount int
}

func fetchABaldBuy() *BaldGuy {
	baldBuy := &BaldGuy{
		Name:      "Daniel Gospodinow",
		HairCount: 0,
	}

	// Doing the nasty thing.
	baldBuy = nil

	return baldBuy
}

func main() {
	baldGuy := fetchABaldBuy()

	if baldGuy.HairCount > 0 {
		log.Printf("Bald guy %s has %d hairs, he's surely been on a trip to Turkey!", baldGuy.Name, baldGuy.HairCount)
	}
}
