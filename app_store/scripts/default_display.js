$(function () {

    $('select').material_select();

   $('.cart-trigger').leanModal({
      ready: function() {
    }
   });

   $('.cart-trigger').siblings('.range-field').find('.value').text('1');

   $('.cart-trigger').on('click', function(){
        $('#cart_modal').openModal();
          var id = $(this).attr('rel');
          var qnt = $(this).siblings('.select-wrapper').children('.select-dropdown').first().val();
          var dur = $(this).siblings('.range-field').find('.value').text();
          $.ajax({
            url: '/app_store/index.add_to_cart/',
            data: {i: id,
                   d: dur,
                   q: qnt},
            success: function(data) {
              $('#cart_modal').find('.modal-content').html(data);
            },
          });
   });

   $('.mobile-trigger').on('click', function(){
          var id = $(this).attr('rel');
          var qnt = $(this).siblings('.select-wrapper').children('.select-dropdown').first().val();
          var dur = $(this).siblings('.range-field').find('.value').text();
          var mobile = $(this).attr('id');
          $.ajax({
            url: '/app_store/index.add_to_cart/',
            data: {i: id,
                   d: dur,
                   q: qnt,
                   m: mobile},
            success: function(data) {
              $('html').html(data);
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