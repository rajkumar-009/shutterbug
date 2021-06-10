$(document).ready(function(){
    //login functionality with validation
    $("form").submit(function(e){
        e.preventDefault();
        var email = $('#email').val();
        var pass = $('#password').val();
        if(email == ""){
            alert('Please enter the email address');
        }
        else if(pass == ""){
            alert('Please enter the password'); 
        }
        else{
            console.log('Form submitted');
        }

    });
});