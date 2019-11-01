function login() {
    $.post('/login', $('#form_login').serialize())
    .done(function(response) {
        $.notify('Welcome!', 'success');
        $('#menu_login').html('My Area');
        $('#menu_logout_link').css('display', 'inline');
        $.get('/info', function(data) {
            $('#modal_info').html(data).modal();
        });
    })
    .fail(function(xhr, status, error) {
        $.notify(JSON.parse(xhr.responseText).error);
    });
}

function logout() {
    $.get('/logout')
    .done(function(response) {
        $.notify('You are logged out!', 'success');
        $.modal.close();
        $('#menu_login').html('Account');
        $('#menu_logout_link').css('display', 'none');
    })
    .fail(function(xhr, status, error) {
        $.notify(JSON.parse(xhr.responseText).error);
    });
}
