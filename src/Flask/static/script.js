let deferredPrompt;
window.addEventListener('beforeinstallprompt', (event) => {
  // Prevent the mini-infobar from appearing on mobile
  event.preventDefault();
  // Stash the event so it can be triggered later.
  deferredPrompt = event;
  // Update UI to notify the user they can install the PWA
  const installButton = document.getElementById('installButton');
  installButton.style.display = 'block';

  installButton.addEventListener('click', () => {
    // Hide the install button
    installButton.style.display = 'none';
    // Show the install prompt
    deferredPrompt.prompt();
    // Wait for the user to respond to the prompt
    deferredPrompt.userChoice.then((choiceResult) => {
      if (choiceResult.outcome === 'accepted') {
        console.log('User accepted the install prompt');
      } else {
        console.log('User dismissed the install prompt');
      }
      deferredPrompt = null;
    });
  });
});



function clear_button() {
  const element = document.getElementById("query");
  element.value = "";
  const element2 = document.getElementById("target");
  element2.value = "";
}

function example_text() {
  const element = document.getElementById("query");
  element.value = "ACTGCTACTGCT";
  const element2 = document.getElementById("target");
  element2.value = "ACTGCCACTGCT";
  const mode = document.getElementById("mode");
  mode.value = "local";
}

function submit_button() {
  const regex = /^[ATCGatcg]+$/g;
  const query = document.getElementById("query");
  const target = document.getElementById("target");
  const _mode = document.getElementById("mode");
  try {
    let match_query = query.value.match(regex).toString();
    let match_target = target.value.match(regex).toString();
    if (
      match_query &&
      match_target &&
      match_query.length &&
      match_target.length >= 10
    ) {
      //upload to server
      const data = {
        Query: query.value,
        Target: target.value,
        Mode: _mode.value,
        Url: window.location.href,
      };
      console.log(data);
      fetch("/upload", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        redirect: "follow",
        body: JSON.stringify(data),
      }).then((response) => response.json());
      window.alert(
        "Sequence submission uploaded!\n" +
          "Click on 'Get Results' to view results under options."
      );
    } else if (
      match_query &&
      match_target &&
      match_query.length &&
      match_target.length <= 10
    ) {
      window.alert("Please enter sequences with lenght of 10 or more.");
      window.location.reload();
    } else if (_mode.value === "default") {
      window.alert("Please select a mode!");
      window.location.reload();
    }
  } catch (e) {
    window.alert(
      "Something went wrong!\n Please check your input and try again."
    );
    console.log(e);
  }
}

async function get_results() {
  const api = "/api/results";
  const data = await fetch(api);
  if (data.status === 200) {
    window.alert("Results are ready! Redirecting to results page...");
    window.location.href = "/results";
  } else if (data.status === 404) {
    window.alert(
      "No results found! Donkey is still working on it...\nPlease try again later."
    );
    window.location.reload();
  }
}

function delete_file() {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/api/delete");
  xhr.send();
  if (window.location.href === "/") {
    window.alert("File deleted successfully!");
    window.location.reload();
  } else {
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

function submit_button_username(){
  const username = document.getElementById("username");
  if (username.value.length > 0) {
    console.log("Usercookie set successfully:"+ username.value);
  } else {
    alert("Please enter a username!");
  }
}



function handle(elem) {
  switch (elem.value) {
    case "example_text":
      example_text();
      break;
    case "get_results":
      get_results();
      break;
    case "clear_button":
      clear_button();
      break;
    case "delete_file":
      delete_file();
      break;
  }
}

window.onload = function () {
  try{
    // Register service worker for PWA
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('/static/service-worker.js')
        .then((registration) => {
          console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }, (error) => {
          console.log('ServiceWorker registration failed: ', error);
        });
    }
    let frame = document.getElementById("iframe");
    frame.style.height = window.innerHeight / 2 + "px";
    frame.style.width = window.innerWidth / 2 + "px";
    if (navigator.userAgent.indexOf("Firefox") != -1) {
      document.getElementById("qr_btn").style.fontWeight = "normal";
      document.getElementById("delete_btn").style.fontWeight = "normal";
    }
  }catch(e){
    console.log(e);
  }

};

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
