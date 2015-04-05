$(function () {
    $('select').material_select();

    $('.delete-btn').on('click', function(){
      var id = $(this).attr('rel');
      $.ajax({
        url: '/app_store/index.delete_from_cart/',
        data: {i: id},
        success: function(data) {
          if($(data).find('#prompt').length > 0){
            $('#cart').html(data);
          }
          else {
            $('#table').html($(data).find('#table').html());
          }
        },
      });
    });

    $('.login-btn').on('click', function(){
      $.ajax({
        url: '/app_account/login.loginUser/',
        data: {redirect_app: 'app_store',
               redirect_func: 'checkout',
               title: 'Please log in to continue'},
        success: function(data) {
          $('#cart_modal').find('.modal-content').html(data);
        },
      });
    });
});