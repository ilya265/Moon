menuIsOpen = false

function showMenu(){
    if (menuIsOpen == false){
        document.querySelectorAll('.menu_btn')[0].style="background-color:white"
        document.querySelectorAll('.menu_btn div')[0].style="background-color:black"
        document.querySelectorAll('.menu_btn div')[1].style="background-color:black"
        document.querySelectorAll('.menu_btn div')[2].style="background-color:black"

        document.querySelectorAll('.sidebar_column')[0].style="transform:translateY(0%)"
        menuIsOpen = true
    }
    else{
        document.querySelectorAll('.menu_btn')[0].style=""
        document.querySelectorAll('.menu_btn div')[0].style=""
        document.querySelectorAll('.menu_btn div')[1].style=""
        document.querySelectorAll('.menu_btn div')[2].style=""

        document.querySelectorAll('.sidebar_column')[0].style="transform: translateY(-120%)"
        menuIsOpen = false
    }
}