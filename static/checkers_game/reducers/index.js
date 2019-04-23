import {stateHasError, statePlayerTurn, fields, pawns, moves, winner, moveDataTmp, joined, time} from './board-state'
import {combineReducers} from 'redux'

export default combineReducers({
  time,
  pawns,
  fields,
  moves,
  winner,
  moveDataTmp,
  stateHasError,
  statePlayerTurn,
  joined
});
