// Use jQuery to toggle  classes to an element
$(function () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
