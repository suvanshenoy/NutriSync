const express = require('express');
const app = express();

app.post('/api/v1/index', (_req, res) => {
	res.redirect('/HealthCare/home')
});

app.get('/HealthCare/home', (_req, res) => {
  res.send('Welcome to the HealthCare page.');
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

