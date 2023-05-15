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
        const _mode = document.getElementById("mode");
        if(query.value === "" || target.value === "")
        {
            window.alert("Please enter a valid sequence!");
            window.location.reload();
        }
        else if(_mode.value === "default")
        {
            window.alert("Please select a mode!");
            window.location.reload();
        }
        else
        {
            const success=window.alert("Sequence submission uploaded!"+"\n" +
            "Click on 'Get Results' to view results under options.");
            //upload to server
            const data = {"Query":query.value,"Target":target.value,"Mode":_mode.value,"Url":window.location.href};
            console.log(data);
            fetch("/upload", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                redirect: "follow",
                body: JSON.stringify(data)
            }).then(response => response.json()).finally(success)   
        }
}

function get_results(){
    open("/results");
}

function delete_file(){
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/api/delete");
    xhr.send();
    if(window.location.href === "/")
    {
        window.alert("File deleted successfully!");
        window.location.reload();
    }
        else
    {
        window.alert("File deleted successfully! redirecting to home page...");
        window.location.href = "/";
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


window.onload = function() {
    let frame = document.getElementById("iframe");
    frame.style.height = (window.innerHeight)/2 + 'px';
    frame.style.width = (window.innerWidth)/2+ 'px';

    if (navigator.userAgent.indexOf("Firefox") != -1) {
        document.getElementById("qr_btn").style.fontWeight = "normal";
        document.getElementById("delete_btn").style.fontWeight = "normal";
    }
}

function updateCols() {
    if (window.innerWidth < 600) {
    let text_areas = document.querySelectorAll("textarea");
    for (const element of text_areas) {
        element.setAttribute("cols", "45");
    }
    }
}

window.addEventListener("resize", updateCols);
updateCols();
