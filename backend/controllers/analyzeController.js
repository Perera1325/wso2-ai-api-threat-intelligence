const { spawn } = require("child_process");

exports.analyzeUser = (req, res) => {
    const userId = req.params.user;

    const python = spawn("python", ["ai-model/predict.py", userId]);

    let dataString = "";

    python.stdout.on("data", (data) => {
        dataString += data.toString();
    });

    python.stdout.on("end", () => {
        res.json({ result: dataString });
    });

    python.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
};