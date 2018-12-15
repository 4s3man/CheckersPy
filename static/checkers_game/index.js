import React from 'react'
import {render} from 'react-dom'
import {Provider} from 'react-redux'

import configureStore from './store/configureStore'
import Checkers from './checkers'

import "./css/styles.css";
import "./css/dialogWindow.css"
import "./css/link.css"

const store = configureStore();
console.log('index.js debug');

render(
  <Provider store={store}>
    <Checkers/>
  </Provider>,
  document.getElementById('JScheckers')
);


var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    console.log('Websocket connected!');
});
