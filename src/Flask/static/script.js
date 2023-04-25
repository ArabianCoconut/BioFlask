



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


        window.location.href = "http://localhost:5000/api/uploaded";
}

function get_results(){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "http://localhost:5000/result");
    xhr.send();
    open("http://localhost:5000/result");
}


