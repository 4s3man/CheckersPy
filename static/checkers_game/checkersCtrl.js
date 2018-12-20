import React, {Component} from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { fetch as fetchPolyfill } from 'whatwg-fetch'

import {fetchBoardState} from './actions/index'

class CheckersCtrl extends Component{
  buttons(){
    let output = [];
    let s = {
      'leave': {'func':() => serverCmd('/game_controller', 'leave', this.props.fetchBoardState('/moves'))},
      'reset': {'func': () => {}}
    }
    for (var k in s) {
      output = [ ...output, button(k, output.length + 1, s[k].func)];
    }

    return output;
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

function serverCmd(url, cmd, updateFunc, options={}){
      fetchPolyfill(url, {
        method:'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body:JSON.stringify(cmd)
      })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        else return response;
      })
      .then((response) => response.text())
      .then(data => console.log(data))
      .then(() => fetchBoardState('/move'));

}

const mapDispatchToProps = (dispatch) => {
  return {
    fetchBoardState: (url, payload={}) => dispatch(fetchBoardState(url, payload)),
  };
}

export default connect(mapDispatchToProps)(CheckersCtrl);
