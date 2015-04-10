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

    $('.pag-right').on('click', function(){
      if($(".active").next(".page").length > 0) {
        var active = $(".active");
        $(this).toggleClass( "core-selected");
        active.toggleClass( "core-selected active" );
        active.next(".page").toggleClass( "core-selected active" );

        var pages = document.querySelector('core-animated-pages');
        pages.selected = active.next(".page").attr("name")
      }
    });

    $('.pag-left').on('click', function(){
      if($(".active").prev(".page").length > 0) {
        var active = $(".active");
        active.toggleClass( "core-selected active" );
        active.prev(".page").toggleClass( "core-selected active" );

        var pages = document.querySelector('core-animated-pages');
        pages.selected = active.prev(".page").attr("name");
      }
    });

    $('.page').on('click', function(){
      if(!$(this).hasClass(".active")) {
        $(".active").toggleClass( "core-selected active" );
        $('li:contains(' + $(this).text() + ')').toggleClass( "active" );
        console.log($('li:contains(' + $(this).text() + ')'))
        var pages = document.querySelector('core-animated-pages');
        pages.selected = $(this).attr("name");
      }
    });

    $.ajax({
      url: '/app_store/index.show_cart/',
      success: function(data) {
        $('#cart').html(data);
        $('#checkout').hide()
      },
    });

});