import React from 'react'
import {render} from 'react-dom'
import {Provider} from 'react-redux'

import configureStore from './store/configureStore'
import Checkers from './checkers'

import style from "./styles.css";

const store = configureStore();
console.log('index.js debug');

render(
  <Provider store={store}>
    <Checkers/>
  </Provider>,
  document.getElementById('JScheckers')
);
