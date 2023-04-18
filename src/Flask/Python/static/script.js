function clear_button(){
    const element = document.getElementById("text_area");
    element.value = "";
}

function submit_button(){
    const element = document.getElementById("text_area");
    //upload to server
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/upload",mime="application/json");
    const body =JSON.stringify({
        text: element.value
    });
    xhr.send(body);
    open("http://localhost:5000/upload");
    console.log(body);
}
