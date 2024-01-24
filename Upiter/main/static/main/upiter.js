var modal = document.querySelector(".model");
var box = document.querySelector(".modal-box");

var closebtn = document.querySelector(".close");
var btn = document.querySelector(".openmodel");

btn.addEventListener("click" , () => {
    modal.classList.add("open");
    box.classList.add("open");
})

modal.addEventListener("click" , () => {
    modal.classList.remove("open");
    box.classList.remove("open");
})

closebtn.addEventListener("click" , () => {
    modal.classList.remove("open");
    box.classList.remove("open");
})

var elements = document.querySelectorAll(".ppp");

function processValue(element) {
  var originalvalue = element.getAttribute('data-value');
  var last4 = originalvalue.substring(originalvalue.length - 4);
  var newValue = "**** " + last4;
  return newValue;
}

elements.forEach((element)=> {
  element.textContent = processValue(element);
});                                           


