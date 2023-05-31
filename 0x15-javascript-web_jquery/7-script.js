// Use jQuery to fetch data from an API and display on page
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    $('div#character').text(data.name);
  });
});
