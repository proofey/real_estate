// Toggle navbar menu
const navbarMenuToggle = document.getElementById('navbar-menu-toggle');
navbarMenuToggle.addEventListener('click', (e)=> {
    e.preventDefault()
    const navbarMenuDropdown = document.getElementById('navbar-menu-dropdown');
    if(navbarMenuDropdown.classList.contains('d-none')){
        navbarMenuDropdown.classList.remove('d-none');
    }else{
        navbarMenuDropdown.classList.add('d-none');
    }
});