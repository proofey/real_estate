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

// Toggle search bar
const searchBarToggle = document.getElementById('search-bar-toggle');
searchBarToggle.addEventListener('click', (e)=> {
    e.preventDefault();

    const searchBar = document.querySelector('.search');

    if(searchBar.classList.contains('hidden')){
        searchBar.classList.remove('hidden')
    }else{
        searchBar.classList.add('hidden')
    };
});