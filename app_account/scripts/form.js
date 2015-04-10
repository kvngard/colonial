// On page load
$(function () {
    $('#account_form').ajaxForm(function(data) {
        $('.modal-content').html(data);
    });

    // On click
    $('.btn-option').on('click', function(){
      var path = $(this).attr('name');
      console.log(path)
      // ajax
      $.ajax({
        url: path,
        success: function(data) {
            console.log(data);
          $('.modal-content').html(data);
        },
      });
    });
});