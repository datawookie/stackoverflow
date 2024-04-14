CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    date_of_birth DATE,
    salary NUMERIC
);

INSERT INTO employees (id, name, email, salary) VALUES (1, 'Bob', 'bob@gmail.com', 80000);
