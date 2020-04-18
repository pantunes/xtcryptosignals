function open_modal(m, id=undefined) {
    if (m === '') {
        return
    }

    const _m = m.replace('#', '#modal_');

    if (m === '#info') {
        $(_m).on($.modal.OPEN, function (event, modal) {
            $.get('/info', function (data) {
                $('#modal_info_text').html(data);
            });
            $(_m).off($.modal.OPEN)
        });

    } else if (m === '#transaction') {
        $(_m).on($.modal.OPEN, function (event, modal) {
            $.get('/ticker/tokens', function (data) {
                let $dropdown = $('#tx_coin_token');
                $dropdown.empty();
                $.each(data.tokens, function () {
                    $dropdown.append($("<option />").val(this).text(this));
                });
            });
            $(_m).off($.modal.OPEN)
        });

    } else if (m === '#login' || m === '#signup') {
        $(_m).on($.modal.OPEN, function (event, modal) {
            captcha();
            $(_m).off($.modal.OPEN)
        });

    } else if (m === '#rule') {
        $(_m).on($.modal.OPEN, function (event, modal) {

            function get_tokens(handler1, handler2) {
                $.get('/ticker/tokens', function (data) {
                    let $dropdown = $('#rule_coin_token');
                    $dropdown.empty();
                    $.each(data.tokens, function () {
                        $dropdown.append($("<option />").val(this).text(this));
                    });
                    handler1(handler2)
                });
            }

            function get_frequencies(handler) {
                $.get('/ticker/frequencies', function (data) {
                    let $dropdown = $('#rule_interval');
                    $dropdown.empty();
                    $.each(data.frequencies, function () {
                        $dropdown.append($("<option />").val(this).text(this));
                    });
                    if (handler !== null) {
                        handler()
                    }
                });
            }

            let title;
            let submit_button;

            if (id !== undefined) {
                title = 'Change Rule';
                submit_button = 'Change';

                function get_rule() {
                    $.get('/notifications/rule/' + id, function (data) {
                        modal_rule_form_edit_handler = modal_rule_form_edit(id, data);
                        modal_rule_form_delete_handler = modal_rule_form_delete(id);
                        $('#form_button_delete').show();
                    })
                }

                get_tokens(get_frequencies, get_rule);
            } else {
                title = 'Add Rule';
                submit_button = 'Add';

                modal_rule_form_edit_handler = modal_rule_form_add;
                $('#form_button_delete').hide();

                get_tokens(get_frequencies, null);
            }

            // title
            $('#modal_rule > h5').html(title);
            // Button
            $('#submit_form').html(submit_button);

            $(_m).off($.modal.OPEN)
        });
    }

    $(_m).on($.modal.BEFORE_CLOSE, function (event, modal) {
        window.location.hash = '';
        $(_m).off($.modal.BEFORE_CLOSE)
    });

    $(_m).modal();

    window.location.hash = m;
}
