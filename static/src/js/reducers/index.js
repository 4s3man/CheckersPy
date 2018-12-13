import {stateHasError, statePlayerTurn, fields, pawns, moves, winner, moveDataTmp} from './board-state'
import {combineReducers} from 'redux'

export default combineReducers({
  pawns,
  fields,
  moves,
  winner,
  moveDataTmp,
  stateHasError,
  statePlayerTurn
});
