$(function () {

    $('select').material_select();
    $('.button-collapse').sideNav();

    $('.collapsible').collapsible({
      accordion : true
    });

    $('.tooltipped').tooltip({delay: 50});

    $('#notify-btn').on('click', function(){
      $(this).removeClass()
      $(this).html('Sending...');
      $(this).addClass('btn-large disabled');
      $.ajax({
        url: '/app_admin/rentals.send_mass_overdue_emails/',
        success: function(data) {
            $('#notify-btn').html('Nofitications Sent');
        },
      });
    });

    $('#mng-btn').on('click', function(){
      $(this).removeClass()
      $(this).html('Sending...');
      $(this).addClass('btn-large disabled');
      $.ajax({
        url: '/app_admin/rentals.send_manager_report_email/',
        success: function(data) {
            $('#mng-btn').html('Report Sent');
        },
      });
    });

});


