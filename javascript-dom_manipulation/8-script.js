document.addEventListener('DOMContentLoaded', () => {
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    const helloElement = document.querySelector('#hello');
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        helloElement.textContent = data.hello;
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
      });
  });
