document.addEventListener('DOMContentLoaded', () => {

    const header = document.querySelector('header');
    const updateHeaderButton = document.querySelector('#update_header');

    updateHeaderButton.addEventListener('click', () => {
        header.textContent = 'New Header!!!';
    });
});
