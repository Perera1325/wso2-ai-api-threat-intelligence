const backendURL = "http://localhost:5000";

async function loadAllUsers() {
    const tableDiv = document.getElementById("userTable");

    try {
        const response = await fetch(`${backendURL}/analyze-all`);
        const data = await response.json();

        let html = "<table border='1' width='100%'>";
        html += "<tr><th>User</th><th>Risk Score</th><th>Status</th></tr>";

        data.forEach(user => {
            html += `<tr>
                        <td>${user.user}</td>
                        <td>${user.risk_score}</td>
                        <td>${user.status}</td>
                     </tr>`;
        });

        html += "</table>";
        tableDiv.innerHTML = html;

    } catch (error) {
        tableDiv.innerText = "Error loading users.";
    }
}