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


// var users = {{ ussers|safe }};



// const allElements = document.querySelectorAll('.element');

// // Добавляем обработчик события для каждого элемента
// allElements.forEach(elem => {
//   elem.addEventListener('click', function() {
//     // Получаем id элемента
//     const id = this.id;
//     console.log(id);

//     // Находим элементы с классом, соответствующим id
//     const targetElements = document.querySelectorAll('.' + id);
//     console.log(targetElements);

//     // Добавляем класс "open" к найденным элементам
//     targetElements.forEach(targetElement => {
//       if (!targetElement.classList.contains('open')) {
//         targetElement.classList.add('open');
//       }
//     });

//     // Удаляем класс "open" у всех остальных элементов
//     allElements.forEach(otherElement => {
//       if (otherElement.id !== id) {
//         const otherTargetElements = document.querySelectorAll('.' + otherElement.id);
//         otherTargetElements.forEach(otherTargetElement => {
//           otherTargetElement.classList.remove('open');
//         });
//       }
//     });
//   });
// });