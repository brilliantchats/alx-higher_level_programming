// Use jQuery to fetch data from an API and display on page
$(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
