$(function () {

    $('select').material_select();
    $('.button-collapse').sideNav();

    $('#search').on('change', function(){
      var param = $('#search').val();
      $.ajax({
        url: '/app_store/index.search/',
        data: {p: param},
        success: function(data) {
          $('.row').html(data);
          $('#search').trigger("blur");
        },
      });
    });

    $('#search').on('keypress', function(e){
      if ((e.keyCode || e.which) == 13) {
          var param = $('#search').val();
          $.ajax({
            url: '/app_store/index.search/',
            data: {p: param},
            success: function(data) {
              console.log(data);
              $('.row').html(data);
              $('#search').trigger("blur");
            },
          });
        }
    });

    $('.cart-trigger').leanModal({
      ready: function() {
    }
   });

   $('.cart-trigger').on('click', function(){
        $('#cart_modal').openModal();
          var id = $(this).attr('rel');
          var qnt = $(this).siblings('.select-wrapper').children('.select-dropdown').first().val();
          $.ajax({
            url: '/app_store/index.add_to_cart/',
            data: {i: id,
                   q: qnt},
            success: function(data) {
              $('#cart_modal').find('.modal-content').html(data);
            },
          });
   });

   $('.cart-display').on('click', function(){
        $('#cart_modal').openModal();
          $.ajax({
            url: '/app_store/index.show_cart/',
            success: function(data) {
              $('#cart_modal').find('.modal-content').html(data);
            },
          });
   });

});


