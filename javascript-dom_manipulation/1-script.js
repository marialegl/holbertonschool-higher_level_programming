document.addEventListener('DOMContentLoaded', () => {

    const header = document.querySelector('header');
    const redHeaderButton = document.querySelector('#red_header');

    redHeaderButton.addEventListener('click', () => {
      header.style.color = '#FF0000';
    });
  });
 