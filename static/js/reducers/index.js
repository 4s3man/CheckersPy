import {stateHasError, statePlayerTurn, fields, pawns, moves} from './board-state'
import {combineReducers} from 'redux'

export default combineReducers({
  pawns,
  fields,
  moves,
  stateHasError,
  statePlayerTurn
});
