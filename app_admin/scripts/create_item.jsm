$(function () {

    // If no data in form, hide all forms
    $('#sale_item_form').css('display', 'none');
    $('#rental_item_form').css('display', 'none');
    $('#custom_item_form').css('display', 'none');

    %if item_type:
        $('#${item_type.lower()}_form').css('display', 'block');
    %endif


    // On selector change, display appropriate form
    $('#item_type').change(function(){
        if ($('#item_type').val()=='store_item'){
            $('#rental_item_form').css('display', 'none');
            $('#custom_item_form').css('display', 'none');
            $('#sale_item_form').css('display', 'block');
        }
        else if ($('#item_type').val()=='rental_item'){
            $('#sale_item_form').css('display', 'none');
            $('#custom_item_form').css('display', 'none');
            $('#rental_item_form').css('display', 'block');
        }
        else {
            $('#sale_item_form').css('display', 'none');
            $('#rental_item_form').css('display', 'none');
            $('#custom_item_form').css('display', 'block');
        }
    });

});


