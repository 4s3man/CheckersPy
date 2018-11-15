import {stateHasError, stateFetchSuccess, statePlayerTurn} from './board-state'
import {pawnClicked} from './moves.js'
import {combineReducers} from 'redux'

export default combineReducers({
  stateFetchSuccess,
  stateHasError,
  statePlayerTurn,
  pawnClicked
});
