function greet(name: string): string {
    return `Hello, ${name}!`;
}

// Main function to execute
function main() {
    const name: string = "World";
    const message: string = greet(name);
    console.log(message);
}

// Call the main function
main();
