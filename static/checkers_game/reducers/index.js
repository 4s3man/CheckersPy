import {stateHasError, statePlayerTurn, fields, pawns, moves, winner, moveDataTmp, joined, time, gameStarted, movingColor} from './board-state'
import {combineReducers} from 'redux'

export default combineReducers({
  movingColor,
  gameStarted,
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
