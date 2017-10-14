function addInput() {
  var newInput = document.createElement('input');
  newInput.setAttribute('placeholder', 'My other Friend\'s Location')
  var container = document.createElement('div');
  container.appendChild(newInput);

  var before = document.getElementById('add-field').parentNode;

  document.getElementById('form').insertBefore(container, before);
}

function delInput() {
  var formChildren = document.getElementById('form').children;
  var lastInputIndex = -1;
  for(var i = 0; i < formChildren.length; i++) {
    if(formChildren[i].children.length >= 1 &&
       formChildren[i].children[0].tagName === 'INPUT') {
      lastInputIndex = i;
    }
  }

  if(lastInputIndex >= 0) {
    formChildren[lastInputIndex].remove();
  }
}

function calculate(stations, callback) {
  var myHeaders = new Headers();
  myHeaders.set('Content-Type', 'application/json');

  var myInit = {
    method : 'POST',
    headers : myHeaders,
    mode : 'cors',
    body : JSON.stringify(stations)
  };

  fetch(new Request('/api/v1/meetup', myInit)).then(res => {
    if(res.ok) {
      return res.blob();
    } else {
      alert("Error in communication with the web server");
    }
  }).then(blob => {
    var reader = new FileReader();
    reader.addEventListener('loadend', () => {
      var result  = JSON.parse(reader.result);
      callback(result);
    });
      reader.readAsText(blob);
  });
}

function showMeeting() {
  var stations = []
  var formChildren = document.getElementById('form').children;
  for(var i = 0; i < formChildren.length; i++) {
    if(formChildren[i].children.length >= 1 &&
      formChildren[i].children[0].tagName === 'INPUT' &&
      formChildren[i].children[0].value !== '') {
      stations = stations.concat([formChildren[i].children[0].value]);
    }
  }

  if(stations.length >= 2) {
    calculate(stations, result => {
      var form = document.getElementById("form");
      var resultDiv = document.getElementById('result');
      if(resultDiv === null) {
        resultDiv = document.createElement('div');
        resultDiv.id = "result";
        form.appendChild(resultDiv);
      }
      resultDiv.innerHTML = "Your Meeting Point is <strong>" + result.meetup + "</strong>";
    });
  }
}

function init() {
  document.getElementById('add-field').onclick = addInput;
  document.getElementById('del-field').onclick = delInput;
  document.getElementById('calc').onclick = showMeeting;
}

window.addEventListener("DOMContentLoaded", init);
