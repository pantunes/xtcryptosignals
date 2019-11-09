const menu_options = ['#menu_portfolio_link', '#menu_logout_link'];

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
        if (window.location.pathname.includes('/portfolio/')) {
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
