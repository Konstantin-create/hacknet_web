let active_window = 'old'
document.getElementById('img-3').className = 'aside-img active-page'
document.getElementById('header-nav-1').className = 'header-nav-item active'
document.getElementById('new-posts').className = 'new-posts hide-item'
let numOfPosts = document.getElementsByClassName('post').length;
document.getElementsByTagName('main')[0].style.height = (numOfPosts * 500 + 250).toString() + 'px'
document.getElementsByTagName('aside')[0].style.height = (numOfPosts * 500 + 250).toString() + 'px'

function change_active() {
    if (active_window == 'old') {
        active_window = 'new'
        document.getElementById('header-nav-1').className = 'header-nav-item'
        document.getElementById('header-nav-2').className = 'header-nav-item active'
        document.getElementById('old-posts').className = 'old-posts hide-item'
        document.getElementById('new-posts').className = 'new-posts'
    } else {
        active_window = 'old'
        document.getElementById('header-nav-1').className = 'header-nav-item active'
        document.getElementById('header-nav-2').className = 'header-nav-item'
        document.getElementById('old-posts').className = 'old-posts'
        document.getElementById('new-posts').className = 'new-posts hide-item'
    }
}