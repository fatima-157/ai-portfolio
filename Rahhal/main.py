// Sample structure for tourism/culture endpoint in the application
const express = require('express');
const router = express.Router();

// Mock database of cultural spots for Team Rahhal MVP
const culturalSpots = [
    { id: 1, name: "Historical Heritage Site", category: "Culture", rating: 4.8 },
    { id: 2, name: "Local Artisan Souq", category: "Tourism", rating: 4.6 }
];

router.get('/api/spots', (req, res) => {
    res.json({
        success: true,
        count: culturalSpots.length,
        data: culturalSpots
    });
});

module.exports = router;
