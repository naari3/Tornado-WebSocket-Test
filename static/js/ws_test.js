var socket = new WebSocket('ws://' + location.host + '/tokenize');

socket.onmessage = function (message) {
  // console.log(message);
  message = JSON.parse(message.data);
  app.results.unshift({
    text: message.text
  });
}


function send_message () {
  text_box = document.getElementById('text_box');
  former_text = text_box.value;
  message = JSON.stringify({
    text: former_text,
  })
  socket.send(message);
  text_box.value = "";
}
