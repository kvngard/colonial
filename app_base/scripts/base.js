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

  function fade() {
    $('.fade').each(function() {
      /* Check the location of each desired element */
      var objectBottom = $(this).offset().top + $(this).outerHeight();
      var windowBottom = $(window).scrollTop() + $(window).innerHeight();

      /* If the object is completely visible in the window, fade it in */
      if (objectBottom < windowBottom) {
        if ($(this).css('opacity')==0) {$(this).fadeTo(500,1);}
      } else {
        if ($(this).css('opacity')==1) {$(this).fadeTo(500,0);}
      }
    });
  }
  fade(); //Fade in completely visible elements during page-load
  $(window).scroll(function() {fade();}); //Fade in elements during scroll

});