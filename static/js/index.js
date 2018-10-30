import React from 'react'
import ReactDOM from 'react-dom'

import Checkers from './checkers'

console.log('dono');
var s = sessionStorage.getItem('board_state')
console.log(s);

ReactDOM.render(<Checkers/>, document.getElementById('JScheckers'));
