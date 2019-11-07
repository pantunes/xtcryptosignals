const menu_options = ['#menu_portfolio_link', '#menu_logout_link'];

function login() {
    $.post('/login', $('#form_login').serialize())
    .done(function(response) {
        $.notify('Welcome!', 'success');
        $('#menu_login').html('My Area');
        let x;
        for (x of menu_options) {
            $(x).css('display', 'inline');
        }
        open_modal('#info');
    })
    .fail(function(xhr, status, error) {
        $.notify(JSON.parse(xhr.responseText).error);
    });
}

function logout() {
    $.get('/logout')
    .done(function(response) {
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
        console.log(xhr.responseText);
        $.notify(JSON.parse(xhr.responseText).error);
    });
}
