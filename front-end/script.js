


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
      // success: function(data) {
      //   console.log(data); 
      // },
      // error: function(xhr, status, error) {
      //     console.log("Error creating user: " + error);
      // }
    })
    $('.hidden-div').empty();
    var head = $('<p>').text('Användare skapad');
    $('.hidden-div').append(head);
  });
});


