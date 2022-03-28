$().ready(function () {

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
        minlength: "Please Enter Min 3 Charcter"
      },
      email: {
        required: "Please Enter Email Id",
        email: "Please Enter Valid Email Id"
      },
      msg: {
        required: "Please Enter Massage",
        maxlength: "Please Enter Max 100 Charcter"
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
