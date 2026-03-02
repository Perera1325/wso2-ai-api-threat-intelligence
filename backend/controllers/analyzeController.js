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
        res.json({ result: dataString.trim() });
    });

    python.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
};