$(function () {

  $('.button-collapse').sideNav();
  $('.parallax').parallax();

  $('a[href*=#]:not([href=#])').click(function() {
      if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
          || location.hostname == this.hostname) {

          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
             if (target.length) {
               $('html,body').animate({
                   scrollTop: target.offset().top
              }, 1000);
              return false;
          }
      }
  });
  
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
});