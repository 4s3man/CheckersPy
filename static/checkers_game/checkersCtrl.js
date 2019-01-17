import React, {Component} from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { fetch as fetchPolyfill } from 'whatwg-fetch'
import {fetchBoardState} from './actions/index'

class CheckersCtrl extends Component{
  constructor(props) {
   super(props);
   this.actionSufix = this.props.actionSufix || '';
   this.url = this.props.actionSufix ? '/move_' + this.props.actionSufix : '/move';
   if ('' === this.actionSufix)console.log('Missing actionSuffix in CheckersCtrl. Please provide valid one.');
  }
  buttons(){
    let output = [];
    var refreshBoard = () => this.props.fetchBoardState(this.url);
    let s = this.actionSufix != 'through_net'? {
      'play again': {'func': () => this.requestAction('/game_controller', 'reset_' + this.actionSufix).then(data => {

          refreshBoard();
        })
      },
      'leave': {'func':() => this.requestAction('/game_controller', 'leave_' + this.actionSufix)
                            .then(data => data !== 'unsuported_action' ? window.location.assign(data) : console.log(data))}
    } :
        {
        'leave': {'func':() => this.requestAction('/game_controller', 'leave_' + this.actionSufix)
                      .then(data => data !== 'unsuported_action' ? window.location.assign(data) : console.log(data))}

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
      <div className='game__ctrl ctrl'>
      {this.buttons()}
      </div>
    );
  }
}

const button = (text, id, func) => {
  return (
    <div key={id} onClick={() => func()} className='ctrl__item button button--ctrl'>{text}</div>
  );
}

const ctrlDispathToProps = (dispatch) => {
  return {
    fetchBoardState: (url, payload={}) => dispatch(fetchBoardState(url, payload)),
  };
}

export default connect(null, ctrlDispathToProps)(CheckersCtrl);
