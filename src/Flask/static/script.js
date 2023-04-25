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
            headers: {
            "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });
    }

function get_results(){
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "http://localhost:5000/results");
    xhr.send();
    open("http://localhost:5000/results");
}
