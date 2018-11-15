import {stateHasError, stateFetchSuccess, statePlayerTurn} from './board-state'
import {pawnChoosed} from './moves.js'
import {combineReducers} from 'redux'

export default combineReducers({
  stateFetchSuccess,
  stateHasError,
  statePlayerTurn,
  pawnChoosed
});
