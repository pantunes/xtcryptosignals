const menu_options_logged_in = [
    '#menu_portfolio_link',
    '#menu_transactions_link',
    '#menu_logout_link',
    '#menu_notifications_link',
];

const urls_logout_to_index = [
    '/transactions',
    '/portfolio',
    '/notifications',
];

function signup() {
    $.post('/signup', $('#form_signup').serialize()).done(function(response) {
        $.notify('Signup completed! You are ready to login!', 'success');
        $.modal.close();
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function login() {
    $.post('/login', $('#form_login').serialize()).done(function(response) {
        $.notify('Welcome!', 'success');
        $('#menu_login').html('My Area');
        for (let x of menu_options_logged_in) {
            $(x).css('display', 'inline');
        }
        open_modal('#info');
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function logout() {
    $.get('/logout').done(function(response) {
        if (urls_logout_to_index.includes(window.location.pathname)) {
            window.location.href = '/';
            return
        }
        $.notify('You are logged out!', 'success');
        $.modal.close();
        $('#menu_login').html('Account');
        for (let x of menu_options_logged_in) {
            $(x).css('display', 'none');
        }
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_transactions(handler) {
    $.get('/transactions/list').done(function(response) {
        handler(response)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_portfolio(handler) {
    $.get('/portfolio/list').done(function(response) {
        handler(response)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_notifications(handler1, handler2=null, coin_token='ALL') {
    $.get('/notifications/list?coin_token=' + coin_token).done(function(response) {
        handler1(response);
        if (handler2) {
            handler2(response)
        }
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_rules(handler) {
    $.get('/notifications/rules').done(function(response) {
        handler(response)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_crypto_fear_greed_index(handler) {
    $.get('/parties/cfgi').done(function(response) {
        handler(response)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_chart_cfgi_btc_data(handler, frequency) {
    $.get('/charts/cfgi/BTC/' + frequency).done(function(response) {
        handler(response, frequency)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_chart_coin_or_token_data(handler, coin_or_token, frequency) {
    $.get('/charts/' + coin_or_token + '/' + frequency).done(function(response) {
        handler(response, coin_or_token, frequency)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function captcha() {
    const _captcha_ids = ['login_image_captcha', 'signup_image_captcha'];
    for (const x of _captcha_ids) {
        $.get('/parties/captcha', function (data) {
            document.getElementById(x).setAttribute(
                'src', `data:image/png;base64,${data['captcha']}`
            );
        });
    }
}
