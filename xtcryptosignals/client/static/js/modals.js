function open_modal(m) {
    if (m === '') {
        return
    }

    if (m === '#modal_info') {
        $(m).on(
            $.modal.OPEN, function (event, modal) {
                $.get('/info', function (data) {
                    $('#modal_info_text').html(data);
                });
            });
    } else if (m === '#modal_transaction') {
        $(m).on(
            $.modal.OPEN, function (event, modal) {
                $.get('/ticker/tokens', function (data) {
                    let $dropdown = $('#tx_coin_token');
                    $dropdown.empty();
                    $.each(data.tokens, function () {
                        $dropdown.append($("<option />").val(this).text(this));
                    });
                });
            });
    }

    $(m).on(
        $.modal.BEFORE_CLOSE, function (event, modal) {
            location.hash = '';
        });

    $(m).modal();
    location.hash = m;
}
