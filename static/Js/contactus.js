$().ready(function () {
  $("textarea").keyup(function(){

    if(this.value.length <= 100){
        $("#remainingChar").html("Remaining Characters : " + (100 - this.value.length));
    } 
    else{
        $("#remainingChar").html("Length Exceeded!");
    }
    });
  $("#form").validate({
    errorElement: 'span',
    rules: {
      name: {
        required: true,
        minlength: 3,
      },
      email: {
        required: true,
        email: true,
      },
      msg: {
        required: true,
        maxlength: 100,
      },

    },

    messages: {
      name: {
        required: "Please Enter Name",
        minlength: "Please Enter Minimum 3 Characters"
      },
      email: {
        required: "Please Enter Email Id",
        email: "Please Enter Valid Email Id"
      },
      msg: {
        required: "Please Enter Message",
        maxlength: "Please Enter Character Less than 100 "
      },
    },
    submitHandler: function (form) {
      alert("Form Submitted");
      console.log('Form Submitted');
      // It is optional submit form or use AJAX snippet here to make AJAX call
      form.submit();
  }
  });

});
