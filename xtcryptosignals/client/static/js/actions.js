const menu_options_logged_in = [
    '#menu_favourites_link',
    '#menu_portfolio_link',
    '#menu_transactions_link',
    '#menu_logout_link',
    '#menu_notifications_link',
    '#menu_exchanges_link',
    '#menu_binance_link',
    '#menu_uniswap_link',
];

const urls_logout_to_index = [
    '/ticker/favourites/10s',
    '/transactions',
    '/portfolio',
    '/notifications',
    '/exchange/binance',
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

function get_chart_cfgi_btc_data(handler, quote, frequency) {
    $.get('/charts/cfgi/BTC/' + frequency).done(function(response) {
        handler(response, quote, frequency)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_chart_coin_or_token_data(handler, coin_or_token, quote, frequency) {
    $.get('/charts/' + coin_or_token + '/' + frequency).done(function(response) {
        handler(response, coin_or_token, quote, frequency)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_chart_tether_data(handler, coin_or_token, quote, frequency) {
    $.get('/charts/tether/' + coin_or_token + '/' + frequency).done(function(response) {
        handler(response, coin_or_token, quote, frequency)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_chart_twitter_data(handler, project, frequency) {
    $.get('/charts/twitter/' + project + '/' + frequency).done(function(response) {
        handler(response, project, frequency)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function captcha() {
    const _captcha_ids = [
        'login_image_captcha',
        'signup_image_captcha',
        'contact_image_captcha'
    ];
    $.get('/parties/captcha', function (data) {
        for (const x of _captcha_ids) {
            document.getElementById(x).setAttribute(
                'src', `data:image/png;base64,${data['captcha']}`
            );
        }
    });
}

function get_favourite(coin_or_token) {
    $.get('/favourites/' + coin_or_token).done(function(response) {
        $(".fa").toggleClass("fa fa-star").toggleClass("fa fa-star-o")
    })
}

function toggle_favourite(coin_or_token) {
    $.post('/favourites/' + coin_or_token).done(function(response) {
        $(".fa").toggleClass("fa fa-star").toggleClass("fa fa-star-o")
    })
    .fail(function(xhr, status, error) {
        if (xhr.status === 401) {
            open_modal('#login');
        }
    });
}

function ping(handler, exchange) {
    $.get(`/exchange/${exchange}/account/status`).done(function(response) {
        handler(response)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_balance(handler, exchange) {
    $.get(`/exchange/${exchange}/balance`).done(function(response) {
        handler(response)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_open_orders(handler, exchange) {
    $.get(`/exchange/${exchange}/orders/open`).done(function(response) {
        handler(response)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}
