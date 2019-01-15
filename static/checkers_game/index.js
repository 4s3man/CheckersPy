//socketio attached in script above in layout.html
import React from 'react'
import {render} from 'react-dom'
import {Provider} from 'react-redux'

import configureStore from './store/configureStore'
import Checkers from './checkers'
import CheckersCtrl from './checkersCtrl'
import Connection from './connection'

import "./css/game.css"
import "./css/dialogWindow.css"

const store = configureStore();
console.log('index.js debug');

export function renderGame(moveUrl, actionSufix){
  render(
    <Provider store={store}>
      <div className='game'>
        <CheckersCtrl moveUrl={moveUrl} actionSufix={actionSufix}/>
        <Checkers moveUrl={moveUrl} actionSufix={actionSufix}/>
      </div>
    </Provider>,
    document.getElementById('JS-checkers')
  );
}

export function renderGame__withConnection(moveUrl, actionSufix){
  render(
    <Provider store={store}>
      <div className='game'>
        <Connection/>
        {/*<Checkers moveUrl={moveUrl} actionSufix={actionSufix} through_net={true}/>*/}
      </div>
    </Provider>,
    document.getElementById('JS-checkers')
  );
}
