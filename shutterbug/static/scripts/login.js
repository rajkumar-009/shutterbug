$(document).ready(function(){
    //login functionality with validation
    $("#login").click(function(e){
        e.preventDefault();
        var username = $('#username').val();
        var pass = $('#password').val();
        if(username == ""){
            alert('Please enter the username');
        }
        else if(pass == ""){
            alert('Please enter the password'); 
        }
        else{
            console.log('Form submitted');
            $("#loginForm").submit();
        }

    });
});