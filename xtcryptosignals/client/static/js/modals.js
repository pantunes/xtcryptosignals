function setup_modals() {
    const modals = ['#contact', '#login', '#signup', '#info', '#transaction'];
    let x;
    for (x of modals) {
        if (window.location.hash !== x) {
            continue
        }
        let m = x.replace('#', '#modal_');
        $(m).modal();
        $(m).on(
            $.modal.AFTER_CLOSE, function(event, modal) {
                location.hash = '';
        });
    }
}

function open_modal(x) {
    $(x).modal();
    location.hash = x.replace('modal_', '');
}
