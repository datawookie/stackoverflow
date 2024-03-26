// Function to sleep for a specified amount of time
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  // Function to check if MongoDB is ready
  async function waitForMongo() {
    let isMongoReady = false;
    const adminDb = db.getSiblingDB('admin');

    while (!isMongoReady) {
      try {
        // Try a simple command to see if MongoDB is ready
        const result = adminDb.adminCommand('ping');
        isMongoReady = result.ok === 1;
        print('🟩 MongoDB is ready.');
      } catch (err) {
        // If an error occurs, MongoDB is not ready, wait for a bit before retrying
        print('⏰ Waiting for MongoDB to be ready...');
        await sleep(1000); // Wait for 1 second before retrying
      }
    }
  }

  // Main function to run the replica set initiation
  async function main() {
    await waitForMongo(); // Wait for MongoDB to be ready
    // Once MongoDB is ready, initiate the replica set
    const result = rs.initiate();
    if (result.ok === 1) {
      print('🟢 Replica set initiated successfully.');
    } else {
      print('🔴 Failed to initiate replica set:', result);
    }
  }

  main().catch(err => print('Error initiating replica set:', err));
