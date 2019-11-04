function setup_modals() {
    const modals = ['#contact', '#login', '#signup', '#info', '#transaction'];
    let x;
    for (x of modals) {
        if (window.location.hash !== x) {
            continue
        }
        let m = x.replace('#', '#modal_');

        if (x === '#info') {
            $(m).on(
                $.modal.OPEN, function(event, modal) {
                    $.get('/info', function(data) {
                        $('#modal_info_text').html(data);
                    });
                });
        }

        $(m).on(
            $.modal.AFTER_CLOSE, function(event, modal) {
                location.hash = '';
        });

        $(m).modal();
    }
}

function open_modal(x) {
    $(x).modal();
    location.hash = x.replace('modal_', '');
}
