document.addEventListener('DOMContentLoaded', () => {

const ulList = document.querySelector('.my_list');
const addItemButton = document.querySelector('#add_item');

addItemButton.addEventListener('click', () => {
    const newLi = document.createElement('li');
    newLi.textContent = 'Item';
    ulList.appendChild(newLi);
})});
