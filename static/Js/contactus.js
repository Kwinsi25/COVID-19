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
      number: {
        required: true,
        maxlength: 10,
        minlength: 10,
      },
      msg: {
        required: true,
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
      number: {
        required: "Please Enter Phone No",
        maxlength: "Please Enter Max 10 Number",
        minlength: "Please Enter Min 10 Number"
      },
      msg: {
        required: "Please Enter Massage",
      },
    },
    submitHandler: function (form) {
      document.getElementById("success").hidden = false;
      form.submit();
  }
  });

});
