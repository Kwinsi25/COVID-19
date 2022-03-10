$().ready(function(){
        
 
        $("#bookAppointmentForm").validate({
            
          
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
                required:"please enter email",
                emailcheck: "please enter valid email"
                
            },
            gender:{
                required: "please select gender",
                
            },
            patientPhone: {
               required : "please enter mobile no.",
               minlength: "length of mobile no. should be 10",
               maxlength: "length of mobile no. should be 10"
            },
            relativePhone: {
                required : "please enter mobile no.",
                minlength: "length of mobile no. should be 10",
                maxlength: "length of mobile no. should be 10"
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