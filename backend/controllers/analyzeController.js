const { spawn } = require("child_process");
const path = require("path");

exports.analyzeUser = (req, res) => {
    const userId = req.params.user;
    const scriptPath = path.join(__dirname, "../../ai-model/predict.py");

    const python = spawn("python", [scriptPath, userId]);

    let dataString = "";

    python.stdout.on("data", (data) => {
        dataString += data.toString();
    });

    python.stdout.on("end", () => {
        if (dataString.includes("|")) {
            const [risk_score, status, confidence] = dataString.trim().split("|");

            res.json({
                user: userId,
                risk_score: parseInt(risk_score),
                status: status,
                confidence: parseFloat(confidence)
            });
        } else {
            res.json({ error: dataString.trim() });
        }
    });

    python.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
};