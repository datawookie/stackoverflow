package main

import (
    "database/sql"
    "fmt"
    "log"
    "os"
    _ "github.com/go-sql-driver/mysql"
)

func main() {
    mysqlHost := os.Getenv("MYSQL_HOST")
    mysqlUser := os.Getenv("MYSQL_USER")
    mysqlPass := os.Getenv("MYSQL_PASS")
    mysqlDatabase := os.Getenv("MYSQL_DATABASE")

    dsn := fmt.Sprintf("%s:%s@tcp(%s:3306)/%s?parseTime=true", mysqlUser, mysqlPass, mysqlHost, mysqlDatabase)

    // Connect to the MySQL database.
    db, err := sql.Open("mysql", dsn)
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    // Test the database connection.
    err = db.Ping()
    if err != nil {
        log.Fatal("Error connecting to the database: ", err)
    }

    fmt.Println("Database Connection Successful!")
}
