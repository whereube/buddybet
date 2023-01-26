/*
function createUser() {
  $.ajax({
    type: "POST",
    url: "http://localhost/create_user",
    data: {
        "name": $("#name").val(),
        "email": $("#email").val(),
        "password": $("#password").val()
      },
      success: function(response) {
          console.log("User created successfully");
      },
      error: function(xhr, status, error) {
          console.log("Error creating user: " + error);
      }
  });

  console.log("hit")
}
*/

$(document).ready(function(){

  $("#createForm").submit(function(){
    $.ajax({
      type: "POST",
      dataType: "json",
      contentType: "application/json",
      url: "http://127.0.0.1:5000/create_user",
      headers: {
        "name": $('#name').val(),
        "email": $('#email').val(),
        "password": $('#password').val()
      }
    })
    .done(console.log("skickat"));
  });

  // $("#createForm").submit(function(){
  //   alert("funkar")
  // });
});


