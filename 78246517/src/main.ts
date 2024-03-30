import "reflect-metadata";
import {createConnection} from "typeorm";

console.log("Connecting to DB...");

createConnection().then(async connection => {
    console.log("Done!");

    const simpleQueryResult = await connection.query('SELECT 1;');
    console.log('Simple query result:', simpleQueryResult);

    const tablesQueryResult = await connection.query('SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname=\'public\';');
    console.log('Tables in public schema:', tablesQueryResult);

}).catch(error => console.log(error));
