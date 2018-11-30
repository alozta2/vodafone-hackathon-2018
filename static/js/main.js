
function changeViewToLoading() {
    document.getElementById("response_loading").style.display = "block";
    document.getElementById("response").style.display = "none";
}

function changeViewToResponse() {
    document.getElementById("response_loading").style.display = "none";
    document.getElementById("response").style.display = "block";
}

function resetToInitialView() {
    document.getElementById("msisdn_text").value = "";
    document.getElementById("response_loading").style.display = "none";
    document.getElementById("response").style.display = "none";
    document.getElementById("msisdn_text").value = "";
}