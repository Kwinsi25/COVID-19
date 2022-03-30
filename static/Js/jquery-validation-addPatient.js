$().ready(function(){
    $("#addPatient").validate({
        rules:{
            patientName : "required",
            phone : {
                required : true,
                minlength:10,
                maxlength: 10
             },
            email : {
                required : true,
                emailcheck : true
             },
            gender : "required",
            patientRelativeName : "required",
            phopatientRelativeContactNumberne : {
                required : true,
                minlength:10,
                maxlength: 10
             },
             line1: "required",
             line2: "required",
             statess :"required",
             cities : "required",
             pincode : "required",
             dob : "required",
             wardss : "required",
             beds : "required",
             prices : "required",
             doctors : "required",
             time : "required",
             symptoms: {required: false},
             history: "required",
             notes: "required",
             file: "required",
        },

        messages:{
            patientName : "Please Enter Patient Name",
            phone : {
                required : "Please Enter Mobile No.",
                minlength: "Length Of Mobile No. Should be 10",
                maxlength: "Length of Mobile No. Should be 10"
             },
            email : {
                required:"Please Enter Email",
                emailcheck: "Please Enter Valid Email"
                
            },
            gender : "Please Select Gender",
            patientRelativeName : "Please Enter Relative Name",
            patientRelativeContactNumber : {
                required : "Please Enter Mobile No.",
                minlength: "Length of Mobile No. Should be 10",
                maxlength: "Length of Mobile No. Should be 10"
             },
            line1 : "Please Enter Address",
            line2 : "Please Enter Address",
            statess : "Please Select State",
            cities : "Please Select City",
            pincode : "Please Enter Pincode",
            dob : "Please Select Date of Birth",
            wardss : "Please Select Ward",
            beds : "Please Select Bed",
            prices : "Please Select Price",
            doctors : "Please Select Doctor",
            time : "Please Select Doctor Visiting Date-Time",
            // symptoms: "Please Select Symptoms",
            history : "Please Enter Any Previous History",
            notes : "Please Enter Doctor notes",
            file : "Please Select File",
        }
    })
    $.validator.addMethod("emailcheck",
            function(value, element) {
                return /^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$/.test(value);
        });

})  