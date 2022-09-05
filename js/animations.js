let last_position = 0

function scroll_handler() {
    let current_position = window.pageYOffset
    let main_header = $('#header')
    let opacity_header = $('#faded-header')

    if (last_position < current_position) {
        if (current_position > 50) {
            main_header.fadeOut('slow')
            opacity_header.fadeIn('slow')
        }
    } else if (last_position > current_position) {
        if (current_position <= 50) {
            main_header.fadeIn('slow')
            opacity_header.fadeOut('slow')
        }
    }
    last_position = current_position
}

window.addEventListener('scroll', scroll_handler)