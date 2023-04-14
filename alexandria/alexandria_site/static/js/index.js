

function openNav() {
    document.getElementById("layoutSidenav").style.width = "150px";
    document.getElementById("shade").style.backgroundColor = "#00000050"
}

function closeNav() {
    document.getElementById("layoutSidenav").style.width = "0";
    document.getElementById("shade").style.backgroundColor = "#00000000"
}

function accordionToggleDown(el){
    acc = el.nextElementSibling.style;
    acc.maxHeight == "100vh" ? acc.maxHeight = "0" : acc.maxHeight = "100vh";
}

function accordionNavToggle(el){
    accNav = document.getElementById("accordionWrapper");
    if(!accNav.classList.contains("nav-active")) accNav.classList.add("nav-active");

    accNavContent = document.getElementById(el.id + "-content").innerHTML;

    accNavContentEl = document.getElementById("accordionNavContent")
    accNavContentEl.innerHTML = accNavContent;

}

function changeSize(el, sizeW, sizeH){
    el.style.width = sizeW;
    el.style.height = sizeH;
}