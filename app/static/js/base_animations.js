function aside_show() {
    let aside = $('#aside')
    let main = $('#main')
    aside.animate({width: 'toggle'}, 360)
    main.css('filter', 'blur(4px)')
}

function aside_hide() {
    let aside = $('#aside')
    let main = $('#main')
    aside.animate({width: 'toggle'}, 360)
    main.css('filter', 'blur(0)')
}