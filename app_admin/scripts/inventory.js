$(function () {

    // Click on filters
    $('#sale_items_filter, #rental_items_filter').on('click', function(){
        var sale_items = $('#sale_items_filter').prop('checked');
        var rental_items = $('#rental_items_filter').prop('checked');
        var params = String(sale_items) + '_' + String(rental_items);
        $.ajax({
            url: '/app_admin/inventory/' + params,
            success: function(data) {
              $('#item_table').html(data);
            }
        });
    })

});


