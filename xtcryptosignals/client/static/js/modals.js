function setup_modals() {
    if (window.location.hash === '#contact') {
        $('#modal_contact').modal();
    }
    else if (window.location.hash === '#login') {
        $('#modal_login').modal();
    }
    else if (window.location.hash === '#signup') {
        $('#modal_signup').modal();
    }
    else if (window.location.hash === '#transaction') {
        $('#modal_transaction').modal();
    }

    $('#modal_contact, #modal_login, #modal_signup').on(
        $.modal.AFTER_CLOSE, function(event, modal) {
            location.hash = '';
    });
}

function open_modal(x) {
    $(x).modal();
    location.hash = x.replace('modal_', '');
}
