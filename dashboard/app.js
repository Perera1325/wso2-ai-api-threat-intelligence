const backendURL = "http://localhost:5000";

async function analyzeUser() {
    const userId = document.getElementById("userId").value;
    const resultElement = document.getElementById("result");

    resultElement.innerText = "Analyzing...";

    try {
        const response = await fetch(`${backendURL}/analyze/${userId}`);
        const data = await response.json();

        if (data.error) {
            resultElement.innerText = data.error;
            return;
        }

        resultElement.innerHTML = `
            Risk Score: ${data.risk_score}/100 <br>
            Status: ${data.status} <br>
            Confidence: ${data.confidence}
        `;
    } catch (error) {
        resultElement.innerText = "Error analyzing user.";
    }
}

checkHealth();