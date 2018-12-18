//io attached in script above in layout.html
import "reset-css"
import "../shared_css/base.css"

var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
    console.log('Websocket connected!');
    socket.emit('create', {})
});
