const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const analyzeController = require("./controllers/analyzeController");

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());

app.get("/", (req, res) => {
    res.json({
        message: "AI API Behavioral Threat Intelligence Service Running"
    });
});

// Analyze specific user behavior
app.get("/analyze/:user", analyzeController.analyzeUser);

// Health check
app.get("/health", (req, res) => {
    res.json({ status: "OK" });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});