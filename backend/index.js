const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(bodyParser.json());
app.use(cors);

// Endpoint to handle the consolidated POST request
app.post('/process', async (req, res) => {
    try {
      const { formData } = req.body;
  
      // Send a GET request to the algorithm service to retrieve the result
      const algorithmResponse = await axios.get('http://localhost:4001/process');

      res.send(algorithmResponse);
  
    } catch (error) {
      console.error('Error processing request:', error);
      res.status(500).json({ error: 'An error occurred while processing the request.' });
    }
  });

app.listen(4000, () => {
    console.log("Listening on port 4000: backend service");
});