function onLoginClick() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) { // Thisis the callback function
            // Get the string data that the server sent us.
            const resultString = this.responseText;

            // Create an object which converts the string to an object using JSON parsing.
            var resultObject = JSON.parse(resultString);

            // Please note, "was_logged_in" is a key set by the server.
            if (resultObject.was_logged_in === false) {
                alert(resultObject.reason);
            } else {
                window.location.href = "{% url 'voc_add' %}";
            }
        }
    }

    xhttp.open("POST", "{{BACKEND_SERVER_ADDRESS}}/api/voc_add", true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    const word = document.getElementById("word").value;
    const explantation = document.getElementById("explantation").value;
    xhttp.send("word="+word);
    xhttp.send("explantation="+explantation);
}

function onBackClick() {
    window.location.href = "{% url 'dashboard_page' %}";
}
