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

function openImgToggle(el){
    shadeBackToggle()
    el.classList.toggle("closed-image");
    el.classList.toggle("open-image");
}

function accordionToggleDown(el){
    panelDown = el.nextElementSibling
    maxH = panelDown.firstElementChild.offsetHeight * panelDown.childElementCount

    acc = panelDown.style;
    acc.maxHeight == "" ? acc.maxHeight = maxH + "px" : acc.maxHeight = "";
}


var running = false
function accordionNavToggle(el){
    function changeContent(){
        accNavContent = document.getElementById(el.id + "-content").innerHTML;

        accNavContentEl = document.getElementById("accordionNavContent")
        accNavContentEl.innerHTML = accNavContent;
    }

    if(running == false){
        if(document.getElementById("accordionNavContent").innerHTML != document.getElementById(el.id + "-content").innerHTML){
            running = true
            accNav = document.getElementById("accordionWrapper");
            transitionDuration = Number(getComputedStyle(accNav).transitionDuration.replace("s", "")) * 1000
            if(!accNav.classList.contains("nav-active")) {
                changeContent();
                accNav.classList.toggle("nav-active");
                running = false
            }else{
                accNav.classList.toggle("nav-active");
                setTimeout(() => {  
                    changeContent(); 
                    accNav.classList.toggle("nav-active"); 
                    running = false; 
                }, transitionDuration);
            }
            
        }
    }
    
}

function changeSize(el, sizeW, sizeH){
    el.style.width = sizeW;
    el.style.height = sizeH;
}