let modals_setup = [];

function open_modal(m) {
    if (m === '') {
        return
    }

    const _m = m.replace('#', '#modal_');

    if (!(modals_setup.includes(_m))) {

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

        } else if (m === '#rule') {
            $(_m).on(
                $.modal.OPEN, function (event, modal) {
                    $.get('/ticker/tokens', function (data) {
                        let $dropdown = $('#rule_coin_token');
                        $dropdown.empty();
                        $.each(data.tokens, function () {
                            $dropdown.append($("<option />").val(this).text(this));
                        });
                    });
                    $.get('/ticker/frequencies', function (data) {
                        let $dropdown = $('#rule_interval');
                        $dropdown.empty();
                        $.each(data.frequencies, function () {
                            $dropdown.append($("<option />").val(this).text(this));
                        });
                    });
                });
        }
    }

    modals_setup.push(_m);

    $(_m).on(
        $.modal.BEFORE_CLOSE, function (event, modal) {
            location.hash = '';
        });

    $(_m).modal();

    location.hash = m;
}
