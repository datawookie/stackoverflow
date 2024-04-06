package main

import (
	"fmt"
	"github.com/h2non/bimg"
)

func main() {
	// options := bimg.Options{
    //     Width:   800,
    //     Height:  600,
    //     Crop:    true,
    //     Quality: 90,
    // }
	_ = bimg.VipsVersion
	fmt.Println("Hello, World!")
}
