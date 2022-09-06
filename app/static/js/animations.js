let last_position = 0

function scroll_handler() {
    let current_position = window.pageYOffset
    let main_header = $('#header')
    let opacity_header = $('#faded-header')

    if (last_position < current_position) {
        if (current_position > 50) {
            main_header.fadeOut(300)
            opacity_header.fadeIn(300)
        }
    } else if (last_position > current_position) {
        if (current_position <= 50) {
            main_header.fadeIn(300)
            opacity_header.fadeOut(300)
        }
    }
    last_position = current_position
}

window.addEventListener('scroll', scroll_handler)