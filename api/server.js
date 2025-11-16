const express = require('express');
const app = express();
const port = process.env.PORT || 3000;


app.get('/', (req, res) => {
res.json({ message: 'API examen', service: 'api', port });
});


app.get('/salud', (req, res) => res.json({ status: 'ok' }));


app.listen(port, () => console.log(`API escuchando en ${port}`));