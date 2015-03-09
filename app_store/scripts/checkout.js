$(function () {
    $('select').material_select();

    $('.btn-flat').on('click', function(){
          var id = $(this).attr('rel');
          console.log(id)
          $.ajax({
            url: '/app_store/index.delete_from_cart/',
            data: {i: id},
            success: function(data) {
              $('#view-box').find('.modal-content').html(data);
            },
          });
    });
});