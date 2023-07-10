// window.onload = function () {
//     window.onscroll = function () {
//         console.log(document.body.scrollTop);
//       if (document.body.scrollTop == 0) {
//         document.getElementById("homeBanner").height = "100vh";
//       }else{
//         document.getElementById("homeBanner").height = "0vh";
//       }
//     };
//   };




function makeFocusable(el){
    el.setAttribute('tabindex', '0');
}

function shadeBackToggle(){
    document.getElementById("shade").classList.toggle("shade-toggle") 
    console.log(document.getElementById("shade").style.backgroundColor)
}

function openNav() {
    document.getElementById("layoutSidenav").style.width = "150px";
    shadeBackToggle()
}

function closeNav() {
    document.getElementById("layoutSidenav").style.width = "0";
    shadeBackToggle()
}

function openImg(el){
    el.classList.toggle("open-image");
}

function accordionToggleDown(el){
    panelDown = el.nextElementSibling
    maxH = panelDown.firstElementChild.offsetHeight * panelDown.childElementCount

    acc = panelDown.style;
    acc.maxHeight == "" ? acc.maxHeight = maxH + "px" : acc.maxHeight = "";
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