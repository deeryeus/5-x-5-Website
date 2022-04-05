const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navCollapse = document.getElementsByClassName('nav-collapse')[0]

toggleButton.addEventListener('click', () => {
    navCollapse.classList.toggle('active')
})

// when user clicks a link on mobile navbar, collapse the navbar
function collapse() {
    navCollapse.classList.toggle('active')
}