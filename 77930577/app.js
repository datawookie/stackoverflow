const fs = require('fs');

const path = '/usr/src/app/data/shared-log.txt';

const id = process.env.ID || 'Default';

const appendContent = () => {
	const now = new Date();
	const timestamp = now.toISOString();
	
	const contentToAdd = `${timestamp}: Data from: ${id}\n`;

	fs.appendFile(path, contentToAdd, err => {
	    if (err) {
		console.error('An error occurred:', err);
		return;
	    }
	    console.log('Line appended successfully');
	});
};

setInterval(appendContent, 5000);
