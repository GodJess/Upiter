document.addEventListener('DOMContentLoaded', function() {
    var selectCard = document.getElementById('selectCard');
    var options = selectCard.querySelectorAll('.getOptions');
    var image = document.getElementById('img');

    selectCard.addEventListener('change', ()=>{
        const selectOption = selectCard.options[selectCard.selectedIndex];
        const img = selectOption.getAttribute('data-img');
        
        image.src = img;
    })

    options.forEach(function(option) {
        var optionValue = option.value;
        var lastFourDigits = optionValue.slice(-4);
        option.textContent = "****" + lastFourDigits;
    });

    var currentDate = new Date().toISOString().slice(0, 10);
    var currentTime = new Date().toTimeString().slice(0, 5);

    // Устанавливаем текущую дату и время в поля ввода
    document.getElementById('dateInput').value = currentDate;
    document.getElementById('timeInput').value = currentTime;

    console.log(currentDate);
    console.log(currentTime);
    

    const cards = document.querySelectorAll('.SelectorCard');
    const fromcard = document.getElementById("fromcard");
    var SelectValue = ""
    cards.forEach( card =>{
        card.addEventListener('click', () => {
            SelectValue = card.getAttribute("data-value");
            fromcard.value = SelectValue;
            console.log(fromcard.value);
            cards.forEach(allElement =>{
                if(allElement.classList.contains('press')){
                    allElement.classList.remove('press');
                }     
            })
            card.classList.add('press');
        })
    });
    
});




