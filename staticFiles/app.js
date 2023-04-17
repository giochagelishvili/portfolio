document.addEventListener("DOMContentLoaded", function() {
    // nav-bar buttons
    const hamburger = document.getElementById("hamburger");
    const closeButton = document.getElementById("close");
    const navMenu = document.getElementById("nav-menu");

    // open menu
    hamburger.addEventListener("click", function() {
        navMenu.style.top = "0";
        document.querySelector("body").style.overflow = "hidden";
    });

    // close menu
    closeButton.addEventListener("click", function() {
        navMenu.style.top = "-100vh";
        document.querySelector("body").style.overflow = "visible";
    });
});