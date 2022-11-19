const dropwdown = document.querySelector('#dropdown');
const menu = document.querySelector('#menudropdown');

const dropwdowncompra = document.querySelector('#dropdowncompra');
const compradropdown = document.querySelector('#compradropdown');

const dropdownalugar = document.querySelector('#dropdownalugar');
const alugardropdown = document.querySelector('#alugardropdown');

const dropdownvenda = document.querySelector('#dropdownvenda');
const vendadropdown = document.querySelector('#vendadropdown');


dropwdown.addEventListener('click', function() {
        menu.classList.toggle('hidden');     
});

dropwdowncompra.addEventListener('click', function() {
        compradropdown.classList.toggle('hidden')
});

dropdownalugar.addEventListener('click', function() {
           alugardropdown.classList.toggle('hidden');
});

dropdownvenda.addEventListener('click', function() {    
        vendadropdown.classList.toggle('hidden');
});

// Path: static\bootstrap\js\script.js