$(document).ready(function(){
    //toggling search button state
    $(".form-control").focusin(function(){
        var city = $("#city").val();
        var baseprice = $("#baseprice").val();
        if(city != "" || baseprice != ""){
            $("#searchButton").prop('disabled',false);
        }
        else{
            $("#searchButton").prop('disabled',true);
        }
    });
    $(".form-control").focusout(function(){
        var city = $("#city").val();
        var baseprice = $("#baseprice").val();
        if(city != "" || baseprice != ""){
            $("#searchButton").prop('disabled',false);
        }
        else{
            $("#searchButton").prop('disabled',true);
        }
    });

    //search functionality
    $("#searchButton").click(function(){
        console.log('search parameters submitted');
        $('#results').removeClass('d-none');
        if(!$('#profileCard').hasClass('d-none')){
            $('#profileCard').addClass('d-none');
        }
        $("#resultsList button").removeClass('active');
    }); 
    
    //reset functionality
    $("#resetButton").click(function(){
        $('#profileCard').addClass('d-none');
        $("#resultsList button").removeClass('active');
        $('#results').addClass('d-none');
        $("#searchButton").prop('disabled',true);
    }); 

    //dynamic profile updation when list item is clicked
    $("#resultsList button").click(function(){
        $("#resultsList button").removeClass('active');
        var element = $(this);
        var name = $(this).children('strong').text();

        if (!element.hasClass('active')){
            element.addClass('active');
        }
        $('#profileCard').removeClass('d-none');
        $('#profileCard').children('strong').text(name);
    });

    $('#bookButton').click(function(){
        var sessionDate = $('#sessionDate').val();
        if(sessionDate == ''){
            alert('Session Date cannot be empty.');
            $('#sessionDate').focus();
        }
        else{
            console.log('Session Booked');
        }
    })
    
});