var socket = new WebSocket('ws://' + location.host + '/tokenize');

socket.onmessage = function (message) {
  // console.log(message);
  message = JSON.parse(message.data);
  app.results.push(message);
}

function send_message () {
  text_box = document.getElementById('text_box');
  former_text = text_box.value;
  message = JSON.stringify({
    former_text: former_text,
  })
  socket.send(message);
  text_box.value = "";
}
