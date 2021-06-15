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
    $("#searchButton").click(function(e){
        e.preventDefault();
        $("#searchForm").submit();
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
        var photographer_id = $(this).val();
        if (!$(this).hasClass('active')){
            $(this).addClass('active');
        }
        $.ajax(
            {
                type:"GET",
                url: "/search",
                data:{
                         id: photographer_id
                },
                success: function( data ) 
                {
                    $('#profileCard').removeClass('d-none');
                    var cardName = data[0].first_name +" " + data[0].last_name
                    $('#cardName').text(cardName);
                    $('#cardCity').text(data[0].city);
                    var cardAddress = data[0].address1 + " " + data[0].address2
                    $('#cardAddress').text(cardAddress);
                    $('#cardBasePrice').text(data[0].base_price);
                    $('#cardPhone').text(data[0].telephone);
                    $('#cardEmail').text(data[0].email);
                }
             })
    });

    $('#bookButton').click(function(){
        var sessionDate = $('#sessionDate').val();
        if(!sessionDate){
            alert('Session Date cannot be empty.');
            $('#sessionDate').focus();
        }
        else {
            var newDate = new Date(sessionDate);
            var today = new Date();
            if (newDate <= today){
                alert('Session Date must be tomorrow or any future dates.');
                $('#sessionDate').focus();
            }
            else {
                console.log('Session Booked!');
            }
        }
    })
    
});