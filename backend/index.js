const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');
const axios = require('axios');

const app = express();
app.use(express.static(path.join(__dirname, '../frontend/build')));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded());
app.use(express.static(path.join(__dirname, '')));
// app.use(cors);

app.get('/', (req, res) => {
    console.log(__dirname);
    res.sendFile(path.join(__dirname, '../frontend/build/index.html'));

})
// Endpoint to handle the consolidated POST request
app.post('/process', async (req, res) => {
    try {
      const data = req.body;
      console.log(data);
      res.redirect('/chatBot.html');
      // Send a GET request to the algorithm service to retrieve the result
      const algorithmResponse = await axios.post('http://127.0.0.1:4001/process', {data});
      console.log(algorithmResponse)

    } catch (error) {
      console.error('Error processing request:', error);
      res.status(500).json({ error: 'An error occurred while processing the request.' });
    }
  });

app.listen(4000, () => {
    console.log("Listening on port 4000: backend service");
});