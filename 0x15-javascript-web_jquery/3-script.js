// Use jQuery to add a class to an element
$(function () {
  $('div#red_header').click(function () {
    $('header').addClass('red');
  });
});
