import React, {Component} from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { fetch as fetchPolyfill } from 'whatwg-fetch'
import {fetchBoardState} from './actions/index'

class CheckersCtrl extends Component{
  constructor(props) {
   super(props);
  }
  buttons(){
    let output = [];
    var refreshBoard = () => this.props.fetchBoardState('/move');
    let s = {
      'leave': {'func':() => this.requestAction('/game_controller', 'leave_' + this.props.actionSufix).then(data => window.location.assign(data))},
      'play again': {'func': () => this.requestAction('/game_controller', 'reset_' + this.props.actionSufix).then(data => refreshBoard()) }
    }

    for (var k in s) {
      output = [ ...output, button(k, output.length + 1, s[k].func)];
    }

    return output;
  }

  requestAction(url, action, options={}){
        return fetchPolyfill(url, {
          method:'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body:JSON.stringify(action)
        })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          else return response;
        })
        .then((response) => response.text())
        //TODO remove log
        // .then(data => {
        //   console.log('Frontend:',data);
        //   return data;
        // })
        .catch((e) => {
          console.log(e);
        });
  }

  render(){
    return (
      <div className='checkers__ctrl'>
      {this.buttons()}
      </div>
    );
  }
}

const button = (text, id, func) => {
  return (
    <div key={id} onClick={() => func()} className='checkers__ctrl__item button button--checkersCtrl'>{text}</div>
  );
}

const ctrlDispathToProps = (dispatch) => {
  return {
    fetchBoardState: (url, payload={}) => dispatch(fetchBoardState(url, payload)),
  };
}

export default connect(null, ctrlDispathToProps)(CheckersCtrl);
