var voltage = document.querySelector('#voltage');
var button = document.querySelector('#button');
const text = document.querySelector('#dynamic-text');
var voltages = 219.57;
voltage.innerHTML = voltages;
button.addEventListener('click', function() {
    location.reload();
})
