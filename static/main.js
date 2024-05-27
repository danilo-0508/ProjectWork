document.addEventListener('scroll', function () {
    var navbar = document.getElementById('navbar');
    var section2 = document.getElementById('section2');
    var section2Top = section2.offsetTop;
    var scrollPosition = window.scrollY;

    if (scrollPosition >= section2Top) {
        navbar.classList.remove('navbar-transparent');
        navbar.classList.add('navbar-colored');
    } else {
        navbar.classList.remove('navbar-colored');
        navbar.classList.add('navbar-transparent');
    }
});

function input(event) {
    let success = document.getElementById("success-box");
    let box = document.getElementById("form-box");
    let error = document.getElementById("emailError");
    let email = document.getElementById("mail");
    let char = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (email.value.match(char)) {
        success.style.display = "block";
        box.style.display = "none";
        event.preventDefault();

        return false;
    } else {
        error.style.display = "block";
        event.preventDefault();

        return false;
    }
}

function dismiss() {
    let success = document.getElementById("success-box");
    let box = document.getElementById("form-box");
    let error = document.getElementById("emailError");
    error.style.display = "none";
    success.style.display = "none";
    box.style.display = "block";
}