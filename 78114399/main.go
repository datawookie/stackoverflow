package main

import (
	"context"
	"fmt"
	"log"

	firebase "firebase.google.com/go"
	"google.golang.org/api/option"
)

func main() {
	// Specify the path to the Firebase configuration file
	configFile := "internal/pkg/utils/firebase/firebaseConfig.json"

	// Initialize the Firebase app with the specified config file
	app, err := firebase.NewApp(context.Background(), nil, option.WithCredentialsFile(configFile))
	if err != nil {
		log.Fatalf("error initializing firebase app: %v", err)
	}

	// Example: Accessing Firestore service from the Firebase app
	// This part is optional and can be replaced with any Firebase service you want to use
	firestore, err := app.Firestore(context.Background())
	if err != nil {
		log.Fatalf("error getting Firestore client: %v", err)
	}
	defer firestore.Close() // Remember to close the Firestore client when done

	// Your Firebase related logic here
	// For demonstration, we'll just print that we've successfully initialized Firestore
	fmt.Println("Successfully initialized Firestore")
}

