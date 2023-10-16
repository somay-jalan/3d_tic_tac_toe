
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const path = require('path');
const app = express();
app.use(bodyParser.json());

const emptyCollection = async () => {
  try {
    await Cube3DModel.deleteMany({});
    console.log('Collection emptied successfully.');
  } catch (error) {
    console.error('Error emptying the collection:', error);
  }
};


// Connect to MongoDB
mongoose.connect('mongodb://localhost/3d_tic_tac_toe', { useNewUrlParser: true, useUnifiedTopology: true });

// Create a MongoDB schema and model
const cube3DSchema = new mongoose.Schema({
  cube_3d: [[Array]]
});

const Cube3DModel = mongoose.model('Cube3D', cube3DSchema);


app.use('/public', express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/single_player_game', (req, res) => {
  res.sendFile(path.join(__dirname, 'single_player_game.html'));
});

app.get('/double_player_game', (req, res) => {
  res.sendFile(path.join(__dirname, 'double_player_game.html'));
});

app.get('/online_player_game', (req, res) => {
  res.sendFile(path.join(__dirname, 'online_player_game.html'));
});

// Handle the POST request to save cube_3d data
app.post('/save_cube_3d/:collectionName', async (req, res) => {
  try {
      const { collectionName } = req.params;  // Get the collection name from the URL parameter

      // Create a MongoDB schema and model for the dynamically generated collection
      const cube3DSchema = new mongoose.Schema({
          cube_3d: [[Array]],
      });

      const DynamicCube3DModel = mongoose.model(collectionName, cube3DSchema);

      const cube3DData = req.body.cube_3d;

      const cube3DInstance = new DynamicCube3DModel({ cube_3d: cube3DData });
      await cube3DInstance.save();

      res.status(200).json({ message: 'Cube 3D data saved successfully.' });
  } catch (error) {
      res.status(500).json({ error: error.message });
  }
});


// Start the server
const port = 3000; // Adjust this port as needed
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

