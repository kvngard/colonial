$(function(){
  $('.signup-trigger').leanModal({
    ready: function() {
      $.ajax({
        url: '/app_account/new.validate_form/',
        success: function(data) {
          $('#signup_modal').find('.modal-content').html(data);
        },
      });
    }
  });

  $('.login-trigger').leanModal({
    ready: function() {
      $.ajax({
        url: '/app_account/login.loginUser/',
        success: function(data) {
          $('#login_modal').find('.modal-content').html(data);
        },
      });
    }
  });

  $('.user-trigger').leanModal({
    opacity: 0,
  });

});