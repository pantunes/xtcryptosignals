const menu_options = [
    '#menu_portfolio_link',
    '#menu_logout_link',
    '#menu_notifications_link',
];

const urls_logout_to_index = [
    '/transactions/portfolio',
    '/notifications',
];

function signup() {
    $.post('/signup', $('#form_signup').serialize()).done(function(response) {
        $.notify('Signup completed!', 'success');
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
        let x;
        for (x of menu_options) {
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
        let x;
        for (x of menu_options) {
            $(x).css('display', 'none');
        }
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_transactions(handler) {
    $.get('/transactions').done(function(response) {
        handler(response)
    })
    .fail(function(xhr, status, error) {
        process_fail(xhr);
    });
}

function get_portfolio(handler) {
    $.get('/portfolio').done(function(response) {
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
