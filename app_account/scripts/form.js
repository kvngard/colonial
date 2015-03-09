$(function () {
    $('#account_form').ajaxForm(function(data) {
        $('.modal-content').html(data);
    });
});