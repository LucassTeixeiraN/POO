let loginContainer = document.getElementById("login-container")
let registerContainer = document.getElementById("register-container")
let inLoginScreen = true

function screenToggle() {
    if(inLoginScreen === true) {
        loginContainer.style.display = "none"
        registerContainer.style.display = "grid"
        inLoginScreen = false
    } else {
        loginContainer.style.display = "grid"
        registerContainer.style.display = "none"
        inLoginScreen = true
    }
}