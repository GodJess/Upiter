var upiter = document.querySelector(".upiter")
var upitermob = document.querySelector(".mobile")
var upiterprem = document.querySelector(".premium")

upiter.addEventListener("click", ()=> {
    if(upitermob.classList.contains("open")){
        upitermob.classList.remove("open");
        document.querySelector(".name-up-mob").classList.remove("open");
        document.querySelector(".number-up-mob").classList.remove("open");
        document.querySelector(".description-up-mob").classList.remove("open");

        upiter.classList.add("open");
        document.querySelector(".name-up").classList.add("open");
        document.querySelector(".number-up").classList.add("open");
        document.querySelector(".description-up").classList.add("open");
    }
    else if(upiterprem.classList.contains("open")){
        upiterprem.classList.remove("open");
        document.querySelector(".name-up-prem").classList.remove("open");
        document.querySelector(".number-up-prem").classList.remove("open");
        document.querySelector(".description-up-prem").classList.remove("open");

        upiter.classList.add("open");
        document.querySelector(".name-up").classList.add("open");
        document.querySelector(".number-up").classList.add("open");
        document.querySelector(".description-up").classList.add("open");
    }

});


upitermob.addEventListener("click", ()=> {
    if(upiter.classList.contains("open")){
        upiter.classList.remove("open");
        document.querySelector(".name-up").classList.remove("open");
        document.querySelector(".number-up").classList.remove("open");
        document.querySelector(".description-up").classList.remove("open");

        upitermob.classList.add("open");
        document.querySelector(".name-up-mob").classList.add("open");
        document.querySelector(".number-up-mob").classList.add("open");
        document.querySelector(".description-up-mob").classList.add("open");
    }
    else if(upiterprem.classList.contains("open")){
        upiterprem.classList.remove("open");
        document.querySelector(".name-up-prem").classList.remove("open");
        document.querySelector(".number-up-prem").classList.remove("open");
        document.querySelector(".description-up-prem").classList.remove("open");

        upitermob.classList.add("open");
        document.querySelector(".name-up-mob").classList.add("open");
        document.querySelector(".number-up-mob").classList.add("open");
        document.querySelector(".description-up-mob").classList.add("open");
    }

});


upiterprem.addEventListener("click", ()=> {
    if(upiter.classList.contains("open")){
        upiter.classList.remove("open");
        document.querySelector(".name-up").classList.remove("open");
        document.querySelector(".number-up").classList.remove("open");
        document.querySelector(".description-up").classList.remove("open");

        upiterprem.classList.add("open");
        document.querySelector(".name-up-prem").classList.add("open");
        document.querySelector(".number-up-prem").classList.add("open");
        document.querySelector(".description-up-prem").classList.add("open");
    }
    else if(upitermob.classList.contains("open")){
        upitermob.classList.remove("open");
        document.querySelector(".name-up-mob").classList.remove("open");
        document.querySelector(".number-up-mob").classList.remove("open");
        document.querySelector(".description-up-mob").classList.remove("open");

        upiterprem.classList.add("open");
        document.querySelector(".name-up-prem").classList.add("open");
        document.querySelector(".number-up-prem").classList.add("open");
        document.querySelector(".description-up-prem").classList.add("open");
    }
   

});
