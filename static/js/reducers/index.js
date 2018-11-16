import {stateHasError, statePlayerTurn, fields, pawns, moves} from './board-state'
import {pawnChoosed} from './moves.js'
import {combineReducers} from 'redux'

export default combineReducers({
  pawns,
  fields,
  moves,
  stateHasError,
  statePlayerTurn,
  pawnChoosed
});
