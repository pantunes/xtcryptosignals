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
        } else if (x === '#transaction') {
            $(m).on(
                $.modal.OPEN, function(event, modal) {
                    $.get('/ticker/tokens', function(data) {
                        let $dropdown = $('#tx_coin_token');
                        $.each(data.tokens, function() {
                            $dropdown.append($("<option />").val(this).text(this));
                        });
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
