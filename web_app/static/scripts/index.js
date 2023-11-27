$(document).ready(function () {
  console.log('ready!');
  $('#signupForm').on('submit', function (event) {
    // alert('Handler for `submit` called.');
    event.preventDefault();
    const form = document.getElementById('signupForm')
    const formData = new FormData(form)
    console.log(formData)
    const payload = {};
    formData.forEach((value, key) => (payload[key] = value));
    // console.log(payload)
    jsonData = JSON.stringify(payload)

    $.ajax({
      url: 'http://localhost:5001/api/v1/users/',
      method: 'POST',
      data: jsonData,
      processData: false,
      contentType: 'application/json',
      success: function (response) {
        // alert('Success!');
        console.log('Successfully signed up')
      },
      error: function (xhr, status, error) {
        // alert('Your form was not sent successfully.');
        console.log(error)
      }
    });
  });
});
