//socketio attached in script above in layout.html
import React from 'react'
import {render} from 'react-dom'
import {Provider} from 'react-redux'

import configureStore from './store/configureStore'
import Checkers from './checkers'
import CheckersCtrl from './checkersCtrl'

import "./css/styles.css"
import "./css/dialogWindow.css"
import "./css/link.css"
import "./css/checkersCtrl.css"

const store = configureStore();
console.log('index.js debug');

export function renderGame(actionSufix){
  render(
    <Provider store={store}>
      <div className='game'>
        <CheckersCtrl actionSufix={actionSufix}/>
        <Checkers/>
      </div>
    </Provider>,
    document.getElementById('JScheckers')
  );
}
