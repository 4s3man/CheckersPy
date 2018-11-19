import {stateHasError, statePlayerTurn, fields, pawns, moves, moveDataTmp} from './board-state'
import {combineReducers} from 'redux'

export default combineReducers({
  pawns,
  fields,
  moves,
  moveDataTmp,
  stateHasError,
  statePlayerTurn
});
