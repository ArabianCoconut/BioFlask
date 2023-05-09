
// Change this to your server link
const server = "http://localhost:5000";

function clear_button(){
    const element = document.getElementById("query");
    element.value = "";
    const element2 = document.getElementById("target");
    element2.value = "";

}

function example_text(){
    const element = document.getElementById("query");
    element.value = "ACTGCT";
    const element2 = document.getElementById("target");
    element2.value = "ACTGCC";
}



function submit_button(){
        const query = document.getElementById("query");
        const target = document.getElementById("target");
        const _mode = document.getElementById("select_mode");
        const success=window.alert("Sequence submission uploaded!"+"\n" +
        "Click on 'Get Results' to view results under options.");
        //upload to server
        const data = {"Query":query.value,"Target":target.value,"Mode":_mode.value};
        fetch("/upload", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            redirect: "follow",
            body: JSON.stringify(data)
        }).then(response => response.json()).finally(success)     
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
    if(window.location.href === server+"/")
    {
        window.alert("File deleted successfully!");
        window.location.reload();
    }
        else
    {
        window.alert("File deleted successfully! redirecting to home page...");
        window.location.href = server+"/";
    }

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

function handle(elem){
    switch (elem.value) {
        case 'example_text':
            example_text();
            break;
        case 'get_results':
            get_results();
            break;
        case 'clear_button':
            clear_button();
            break;
        case 'delete_file':
            delete_file();
            break;
    }
}

