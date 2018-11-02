import {stateHasError, stateFetchSuccess, statePlayerTurn} from './board-state'
import {combineReducers} from 'redux'

export default combineReducers({
  stateFetchSuccess,
  stateHasError,
  statePlayerTurn
});
