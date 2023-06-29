let element = document.querySelector("#warning, #success");

setTimeout(function () {
  if (element) {
    element.style.display = "none";
  }
}, 4000);
