function open_modal(m) {
    if (m === '') {
        return
    }

    const _m = m.replace('#', '#modal_');

    if (m === '#info') {
        $(_m).on(
            $.modal.OPEN, function (event, modal) {
                $.get('/info', function (data) {
                    $('#modal_info_text').html(data);
                });
            });
    } else if (m === '#transaction') {
        $(_m).on(
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

    $(_m).on(
        $.modal.BEFORE_CLOSE, function (event, modal) {
            location.hash = '';
        });

    $(_m).modal();

    location.hash = m;
}
