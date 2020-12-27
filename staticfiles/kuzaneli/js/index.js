
/*Menu handling*/

function disableScroll() {
    document.body.classList.add("stop-scrolling");
}

function enableScroll() {
    document.body.classList.remove("stop-scrolling");
}

function handleChange(checkbox) {
    if(checkbox.checked === true){
        if (window.innerWidth < 768) {
            appear();
        }
    }else{
        disappear();
    }
}

function appear(){
    const animation = document.getElementById("overlay");
    const animationIcon = document.getElementById('icon2');
    const animationNavs = document.getElementById("collapsedNavItems");
    const contactSection = document.getElementById('contact');
    /* Layout display */
    animation.style.display="block";
    animation.style.height="100vh";
    animation.style.animationName="appear";
    animation.style.animationPlayState = "running";
    animation.style.zIndex = "1";
    animation.style.pointerEvents = "auto";
    /* Icon animation */
    animationIcon.style.animationName = "iconTranslateUp"
    animationIcon.style.animationPlayState = 'running';
    animationIcon.style.animationTimingFunction = "ease-out";
    /* Menu items animation*/
    animationNavs.style.animationName = "itemsTranslateUp"
    animationNavs.style.animationPlayState = 'running';
    animationNavs.style.animationTimingFunction = "ease-out";
    /* Contacts block disappearance*/
    contactSection.style.display="none";

    disableScroll();
}

function disappear() {
    const animation = document.getElementById("overlay");
    const animationIcon = document.getElementById('icon2');
    const animationNavs = document.getElementById("collapsedNavItems");
    const contactSection = document.getElementById('contact');
    /* Layout disappearance */

    animation.style.animationName="disappear";
    animation.style.animationPlayState="running";
    animation.style.pointerEvents = "none";
    /* Icon animation */
    animationIcon.style.animationName = "iconTranslateDown";
    animationIcon.style.animationTimingFunction = "ease-in";
    animationIcon.style.animationPlayState = "running";
    /* Menu items animation*/
    animationNavs.style.animationName = "itemsTranslateDown"
    animationNavs.style.animationPlayState = 'running';
    animationNavs.style.animationTimingFunction = "ease-in";
    const singleEvent = () => {
        animation.style.display="none";
        contactSection.style.display="block";
        animation.removeEventListener('animationend', singleEvent)
        animation.style.height="auto";
        animation.style.zIndex="0";
    }
    animation.addEventListener('animationend', singleEvent);
    enableScroll();
    return false;
}

window.addEventListener('resize', function(){
    const check = document.getElementById('responsive-menu');
    if(check.checked) {
        if (window.innerWidth > 767) {
            disappear();
        }
        else {
            appear();
        }
    }
})



/*handleChange(check)*/

/*
var check = document.getElementById('responsive-menu');
if(check.checked) {
    if (window.innerWidth > 845) {
        check.checked = false;
        if ("createEvent" in document) {
            var evt = document.createEvent("HTMLEvents");
            evt.initEvent("change", false, true);
            check.dispatchEvent(evt);
        } else {
            element.fireEvent("onchange");
        }
    }
}*/