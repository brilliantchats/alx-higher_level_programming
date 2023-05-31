// Use jQuery to update the text in the header element
$(function () {
  $('div#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
