//socketio attached in script above in layout.html
import React from 'react'
import {render} from 'react-dom'
import {Provider} from 'react-redux'

import configureStore from './store/configureStore'
import Checkers from './checkers'

import "../shared_css/base.css"
import "reset-css"

import "./css/styles.css"
import "./css/positioning.css"
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
