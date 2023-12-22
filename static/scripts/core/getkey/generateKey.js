function generateAPIKey() {
    // Make an AJAX request to the Flask endpoint
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "dev/genkey", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Parse the JSON response and update the result div
            var response = JSON.parse(xhr.responseText);
            document.getElementById("apiKeyResult").innerHTML = "<p>Public API Key: <strong>" + response.api_key + "</strong></p>";
            document.getElementById("generateKeyBtn").disabled = true;
            document.getElementById("agreeCheckbox").disabled = true;
        }
    };
    xhr.send();
}
