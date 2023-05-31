// Use jQuery to select an id of a element and change its color
$(function () {
  $('div#red_header').click(function () {
    $(this).css('color', '#FF0000');
  });
});
