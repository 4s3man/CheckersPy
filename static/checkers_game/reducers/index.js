import {stateHasError, statePlayerTurn, fields, pawns, moves, winner, moveDataTmp, joined} from './board-state'
import {combineReducers} from 'redux'

export default combineReducers({
  pawns,
  fields,
  moves,
  winner,
  moveDataTmp,
  stateHasError,
  statePlayerTurn,
  joined
});
