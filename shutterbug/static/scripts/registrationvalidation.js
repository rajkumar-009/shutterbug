$(document).ready(function() {
    $('#submitButton').click(function(e) {
        e.preventDefault();
        var Firstname = document.getElementById('firstname').value;
        var Lastname = document.getElementById('lastname').value;
        var Dateofbirth = document.getElementById('dateofbirth').value;
        var Email = document.getElementById('email').value;
        var gender = document.getElementById('gender').value;


        var Username = document.getElementById('username').value;
        var Password = document.getElementById('password').value;
        var Address1 = document.getElementById('address').value;
        var Address2 = document.getElementById('address2').value;
        var City = document.getElementById('city').value;
        var State = document.getElementById('state').value;
        var Zip = document.getElementById('zip').value;
        var Telephone = document.getElementById('phone').value;

        var accountType = document.getElementById('accounttype').value;
        



        const Lname = Lastname.trim();
        const dob = Dateofbirth.trim();
        const emailId = Email.trim();
        const Uname = Username.trim();
        const pwd = Password.trim();
        const adr = Address1.trim();
        const adr2 = Address2.trim();
        const cityname = City.trim();
        const Statename = State.trim();
        const Zipnumber = Zip.trim();
        const TelephoneNumber = Telephone.trim();


        if (Firstname == '') {
            alert("First name can't be empty");
            document.getElementById('firstname').focus();
            return false;
        }
        if (Lname == '') {
            alert("Last name can't be empty");
            document.getElementById('lastname').focus();
            return false;
        }

        if (dob == '') {
            alert("date of birth can't be empty");
            document.getElementById('dateofbirth').focus();
            return false;
        }

        if (emailId == '') {
            alert("Email can't be empty");
            document.getElementById('email').focus();
            return false;
        }

        var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        if (!emailId.match(mailformat)) {
            alert("You have entered an invalid email address!");
            document.getElementById('email').focus();
            return false;
        }

        if (!gender == '' &&
            !gender == 'Choose gender') {
            alert("Gender can't be empty");
            return false;
        }


        if (Uname == '') {
            alert("User name can't be empty");
            document.getElementById('username').focus();
            return false;
        }

        if (Uname.length < 8) {
            alert("User name can't be less than 8 characters");
            document.getElementById('username').focus();
            return false;
        }

        if (Uname.match(/[^\w\.\-]/)) {
            alert("Special characters are not allowed");
            document.getElementById('username').focus();
            return false;
        }

        var re = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;
        if (!re.test(pwd)) {
            alert("Please provide a password meeting the suggested criteria");
            document.getElementById('password').focus();
            return false;
        }

        if (pwd.length < 8) {
            alert("Password can't be less than 8 characters");
            document.getElementById('password').focus();
            return false;
        }

        if (adr == '') {
            alert("Address line 1 can't be empty");
            document.getElementById('address').focus();
            return false;
        }

        if (cityname == '') {
            alert("City can't be empty");
            document.getElementById('city').focus();
            return false;
        }

        if (Statename == 'Select US State') {
            alert("Please choose any one state");
            document.getElementById('state').focus();
            return false;
        }
        if (Zipnumber == '') {
            alert("Zip can't be empty");
            document.getElementById('zip').focus();
            return false;
        }
        if (TelephoneNumber == '') {
            alert("Telephone can't be empty");
            document.getElementById('phone').focus();
            return false;
        }
        if (!accountType == '' &&
            !accountType == 'Choose account type') {
            alert("Account type is Mandatory");
            document.getElementById('accounttype').focus();
            return false;
        }
        if(accountType == 'Photographer account'){
            var baseprice = document.getElementById('baseprice').value;
            if (baseprice == '' || baseprice < 0) {
                alert("Base Price can't be empty or negative");
                document.getElementById('baseprice').focus();
                return false;
            }

        }
        //console.log('form validated and submitted');
        $("#form").submit();
    });

    $('#accounttype').change(function(){
        if($('#accounttype').val() == 'Photographer account'){
            $('#baseprice').prop('disabled',false);
        }
        else{
            $('#baseprice').prop('disabled',true);
        }
    });
});