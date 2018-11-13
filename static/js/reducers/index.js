import {stateHasError, stateFetchSuccess, statePlayerTurn, pawnClicked} from './board-state'
import {combineReducers} from 'redux'

export default combineReducers({
  stateFetchSuccess,
  stateHasError,
  statePlayerTurn,
  pawnClicked
});
