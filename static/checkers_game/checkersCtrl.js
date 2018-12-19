import React, {Component} from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

class CheckersCtrl extends Component{
  buttons(){
    let output = [];
    let s = {
      'leave': {'func':() => {alert('ok')}},
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
    <div key={id} onClick={()=>func()} className='checkers__ctrl__item button button--checkersCtrl'>{text}</div>
  );
}

export default connect()(CheckersCtrl);
