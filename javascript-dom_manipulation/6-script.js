document.addEventListener('DOMContentLoaded', () => {
    const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

    fetch(apiUrl).then(respose => {
        if (!respose.ok) {
            throw new Error('Network response was not ok');
        }
        return respose.json();
    }).then(data => {
        const characterName = data.name;
        document.querySelector('#character').textContent = characterName;
    }).catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
});
