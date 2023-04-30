
// Change this to your server link
const server = "http://localhost:5000";

function clear_button(){
    const element = document.getElementById("query");
    element.value = "";
    const element2 = document.getElementById("target");
    element2.value = "";

}

function submit_button(){
        const query = document.getElementById("query");
        const target = document.getElementById("target");
        //upload to server
        const data = {"Query":query.value,"Target":target.value};
        fetch("/upload", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            redirect: "follow",
            body: JSON.stringify(data)
        }).then(response => response.json());


        window.location.href = server+"/api/uploaded";
}

function get_results(){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", server+"/result");
    xhr.send();
    open(server+"/result");
}

function delete_file(){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", server+"/api/delete");
    xhr.send();
    window.alert("File deleted successfully! redirecting to home page...");
    window.location.href = server+"/";
}

function togglePopup() {
    if (popupHolder.style.display === "none") {
    popupHolder.style.display = "block";
    } else {
    popupHolder.style.display = "none";
    }
}

window.onclick = function(event) {
    if (event.target === popupHolder) {
        togglePopup();
    }
}