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

    $('.collapsible').collapsible({
      accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    });

    // Click on filters
    $('#custom_item_filter, #sale_items_filter, #rental_items_filter').on('click', function(){
        var custom_items = $('#custom_item_filter').prop('checked');
        var sale_items = $('#sale_items_filter').prop('checked');
        var rental_items = $('#rental_items_filter').prop('checked');
        $.ajax({
            data: {c: custom_items,
                   s: sale_items,
                   r: rental_items},
            url: '/app_store/index.filter/',
            success: function(data) {
              $('.row').html(data);
            }
        });
    })

});


