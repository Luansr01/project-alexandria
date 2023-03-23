function openNav() {
    document.getElementById("mySidenav").style.width = "150px";
    document.getElementById("shade").style.backgroundColor = "#00000050"
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("shade").style.backgroundColor = "#00000000"
}

function makeBig(size){
    document.getElementById("logo").style.fontSize = size;
}

function makeSmall(size){
    document.getElementById("logo").style.fontSize = size;
}