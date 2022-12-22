let active_window = '' // First screen

document.getElementById('img-3').className = 'aside-img active-page'
document.getElementById('header-nav-1').className = 'header-nav-item active'
document.getElementById('old-posts').className = 'old-posts hide-item'


function change_active() {
    if (active_window === 'old') {
        active_window = 'new'
        document.getElementById('header-nav-1').className = 'header-nav-item'
        document.getElementById('header-nav-2').className = 'header-nav-item active'
        document.getElementById('index').className = 'index hide-item'
        document.getElementById('blog-page').className = 'blog-page'
    } else {
        active_window = 'old'
        document.getElementById('header-nav-1').className = 'header-nav-item active'
        document.getElementById('header-nav-2').className = 'header-nav-item'
        document.getElementById('index').className = 'index'
        document.getElementById('blog-page').className = 'blog-page hide-item'
    }
}