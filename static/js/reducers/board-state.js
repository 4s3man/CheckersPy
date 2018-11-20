import * as constants from "../constants/action-types"
import {selectPawn, deselectPawn} from "../actions/moves.js"

export function fields(state = {}, action){
  switch (action.type) {
    case constants.STATE_FETCH_SUCCESS:
      for (let key in action.fields) {
        if (action.fields.hasOwnProperty(key)) {
          let field = action.fields[key];
          if(field.moves.length)field['funcs'] = 'selectPawn';
        }
      }
      return action.fields;

    case constants.SELECT_FIELD_FUNCTIONS_UPDATE:
      let updatedFields = cleanPreviousFieldFunctions(Object.assign({}, state));
      updatedFields[action.field].funcs = 'deselectPawn';
      action.normalizedMoves.forEach((move)=>{
        updatedFields[move.position_after_move] = Object.assign({'funcs':'fetchBoardState'}, updatedFields[move.position_after_move]);
      });
      return updatedFields;

    case constants.DESELECT_FIELD_FUNCTIONS_UPDATE:
      return cleanPreviousFieldFunctions(Object.assign({}, state));;

    default:
      return state;
  }
};

function cleanPreviousFieldFunctions(state) {
  for (let key in state) {
    if (state.hasOwnProperty(key)) {
      if (state[key].funcs === 'fetchBoardState' || state[key].funcs === 'deselectPawn') {
        delete state[key].funcs;
      }
      if(state[key].moves && state[key].moves.length)state[key].funcs = 'selectPawn';
    }
  }
  return state;
}

export function moveDataTmp(state = {}, action){
  switch (action.type) {
    case constants.SAVE_MOVE_DATA_TMP:
      return action.moveData;
    case constants.DESELECT_FIELD_FUNCTIONS_UPDATE:
      return {};
    default:
      return state;
  }
};


export function pawns(state = {}, action){
  switch (action.type) {
    case constants.STATE_FETCH_SUCCESS:
      return action.pawns;

    default:
      return state;
  }
};

export function moves(state = {}, action){
  switch (action.type) {
    case constants.STATE_FETCH_SUCCESS:
      return action.moves;

    default:
      return state;
  }
};

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
