var inputCount = 2;

function addInput() {
  var newInput = document.createElement('input');
  newInput.id = 'friend' + String(inputCount - 1);
  newInput.setAttribute('placeholder', 'My other Friend\'s Location')
  var container = document.createElement('div');
  container.appendChild(newInput);

  var before = document.getElementById('add-field').parentNode;

  document.getElementById('form').insertBefore(container, before);
  inputCount += 1;
}

function init() {
  document.getElementById('add-field').onclick = addInput;
}

window.onload = init; // TODO replace by ES6 stuff
