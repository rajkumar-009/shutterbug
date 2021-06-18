$(document).ready(function(){
    $('.btn-primary').click(function(){
        $(this).parent().next().removeClass('d-none')
    });
    $('.btn-warning').click(function(e){
        e.preventDefault();
        var sessionDate = $(this).prev().val()
        if (sessionDate == ""){
            alert('The new Date must be tomorrow or any future dates.');
            $(this).prev().focus();
        }
        else {
            $(this).parent().submit();
        }
    });
    $(".btn-danger").click(function(){
        $(this).next().removeClass('d-none');
    })
})