package main

import (
    "fmt"
    "log"
    "os"
    _ "github.com/go-sql-driver/mysql"
    "github.com/jmoiron/sqlx"
)

func main() {
    user := os.Getenv("DB_USER")
    password := os.Getenv("DB_PASSWORD")

    connection := fmt.Sprintf("%s:%s@(mysql:3306)/zumenu_db", user, password)

    fmt.Println("Connecting to database: ", connection)
    db, err := sqlx.Connect("mysql", connection)
    if err != nil {
        log.Fatal(err)
    }

    err = db.Ping()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Database connection successful")
}
