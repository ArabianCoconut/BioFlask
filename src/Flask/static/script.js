function clear_button(){
    const element = document.getElementById("text_area");
    element.value = "";
}

function submit_button(){
    const mime="application/json";

    const element = document.getElementById("text_area");
    //upload to server
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/upload", mime);
    const body =JSON.stringify({
        "Data": element.value
    });
    xhr.send(body);
    open("http://localhost:5000/upload");
}