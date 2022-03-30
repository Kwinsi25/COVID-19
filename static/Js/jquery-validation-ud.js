$().ready(function(){
        $("#bookAppointmentForm").validate({
          ignore: [],
          rules : {
            patientName : "required",
            relativeName : "required",
            gender : "required",
            emailId : {
               required : true,
               emailcheck : true
            },
            patientPhone: {
               required : true,
               minlength:10,
               maxlength: 10
            },
            relativePhone: {
                required : true,
                minlength:10,
                maxlength: 10
             },
            reason: "required",
        },
//         errorPlacement:
//  function( error, element ){
//  if(element.is( ":radio" )){
//  // error append here
//  error.appendTo('#mygender');
//  }
//  else {
//  error.insertAfter(element);
//  }
//  },
            messages : {
            patientName : "Please Patient Name",
            relativeName : "Please Patient's Relative Name",      
            emailId:{
                required:"Please enter email",
                emailcheck: "Please enter valid email"
                
            },
            gender:{
                required: "Please select gender",
                
            },
            patientPhone: {
               required : "Please enter mobile no.",
               minlength: "Length of mobile no. should be 10",
               maxlength: "Length of mobile no. should be 10"
            },
            relativePhone: {
                required : "Please enter mobile no.",
                minlength: "Length of mobile no. should be 10",
                maxlength: "Length of mobile no. should be 10"
             },
             reason : "Please enter Reason to Book Appointment",
            
            
        }
        
        });
        $.validator.addMethod("pwcheck",
            function(value, element) {
                return /(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/.test(value);
        });
        $.validator.addMethod("emailcheck",
            function(value, element) {
                return /^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$/.test(value);
        });

        

        });