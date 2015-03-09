$(function(){
  $('.password-trigger').leanModal({
    ready: function() {
      $.ajax({
        url: '/app_account/change_password/',
        success: function(data) {
          $('#password_modal').find('.modal-content').html(data);
        },
    });
    } // Callback for Modal open\
  });
});