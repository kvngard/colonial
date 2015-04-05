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

});


