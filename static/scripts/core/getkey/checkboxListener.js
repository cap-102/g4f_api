document.getElementById("agreeCheckbox").addEventListener("change", function () {
    document.getElementById("generateKeyBtn").disabled = !this.checked;
});
