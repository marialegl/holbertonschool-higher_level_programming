document.addEventListener('DOMContentLoaded', () => {
    const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
    const ulListMovies = document.querySelector('#list_movies');

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
        })
        .then(data => {
          data.results.forEach(film => {
            const li = document.createElement('li');
            li.textContent = film.title;
            ulListMovies.appendChild(li)});
        })
        .catch(error => {
          console.error('There was a problem with the fetch operation:', error);
        });
});
