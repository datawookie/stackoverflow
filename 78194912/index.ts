import express from 'express';
import * as randomstring from 'randomstring';

const app = express();
const port = 3000;

app.get('/', (req, res) => {
  const randomStr: string = randomstring.generate({
    length: 10,
    charset: 'alphabetic'
  });

  res.send(`Your random string: ${randomStr}`);
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}.`);
});
