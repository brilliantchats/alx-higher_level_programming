// Use jQuery to add a li item to a list
$(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
