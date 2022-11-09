let active_window = '' // First screen
let numOfPosts = document.getElementsByClassName('post').length;
let form_screens = ['form-screen1', 'form-screen2']
let form_screen = 0
let progress_bar = document.getElementsByClassName('progress-el')[0]

document.getElementById('img-3').className = 'aside-img active-page'
document.getElementById('header-nav-1').className = 'header-nav-item active'
document.getElementById('old-posts').className = 'old-posts hide-item'

document.getElementsByTagName('main')[0].style.height = '300vh'
document.getElementsByTagName('aside')[0].style.height = '300vh'

for (let i = 1; i <= form_screens.length; i++) {
    document.getElementById(form_screens[i]).className = form_screens[i] + ' hidden'
}

function change_active() {
    if (active_window === 'old') {
        active_window = 'new'
        document.getElementById('header-nav-1').className = 'header-nav-item'
        document.getElementById('header-nav-2').className = 'header-nav-item active'
        document.getElementById('total').className = 'total hide-item'
        document.getElementById('blog-page').className = 'blog-page'
    } else {
        active_window = 'old'
        document.getElementById('header-nav-1').className = 'header-nav-item active'
        document.getElementById('header-nav-2').className = 'header-nav-item'
        document.getElementById('total').className = 'total'
        document.getElementById('blog-page').className = 'blog-page hide-item'
    }
}