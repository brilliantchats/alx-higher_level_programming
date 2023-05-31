// Use jQuery to fetch data from an API and display on page
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const results = data.results;
    for (const result in results) {
      $('ul#list_movies').append(`<li>${results[result].title}</li>`);
    }
  });
});
