import * as constants from "../constants/action-types"
import {choosePawn} from "../actions/moves.js"

export function statePlayerTurn(state = false, action){
  switch (action.type) {
    case constants.PLAYER_TURN:
      return action.playerTurn;

    default:
      return state;
  }
};

export function stateHasError(state = false, action){
  switch (action.type) {
    case constants.STATE_HAS_ERROR:
      return action.hasError;

    default:
      return state;
  }
};

export function stateFetchSuccess(state = {}, action){
  switch (action.type) {
    case constants.STATE_FETCH_SUCCESS:
      return makeFieldsDataFromState(action, state)

    default:
      return state;
  }
};

//TODO do something with this func added here
function makeFieldsDataFromState(action, stateBefore){
  if (action.state['white_pawns'] == undefined) return state;
  let pawns = action.state['white_pawns'].concat(action.state['black_pawns']);
  let fieldsData = {}
  for (let i=0; i<pawns.length; i++){
    if (pawns[i]){
      let key = pawns[i].y + ' ' + pawns[i].x;
      fieldsData[key] = {pawn: pawns[i]};

      if(pawns[i].moves != undefined && pawns[i].moves.length > 0)
        fieldsData[key]['moveFunc'] = choosePawn;
    }
  }
  return fieldsData;
}
