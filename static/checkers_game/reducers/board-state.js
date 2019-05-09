import * as constants from "../constants/action-types"
import {selectPawn, deselectPawn} from "../actions/moves.js"
import {dispatchClearTime} from "../actions";

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
        updatedFields[move.position_after_move] = Object.assign({}, updatedFields[move.position_after_move], {'funcs':'fetchBoardState'});
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

export function winner(winner = '', action){
  switch (action.type) {
    case constants.STATE_FETCH_SUCCESS:
      return action.winner;
    case constants.SET_WINNER:
      return action.winner;

    default:
      return winner;
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

export function joined(state = false, action){
  switch (action.type) {
    case constants.JOINED:
      return action.joined;

    default:
    return state;
  }
};

function getIdOfPawnWithMoves(fields) {
  for (var key in fields) {
    let field = fields[key];
    if (fields.hasOwnProperty(key) && field.moves.length) {
        return field.pawn;
    }
  }
}

export function movingColor(state = 'white', action) {
  if (action.type === constants.STATE_FETCH_SUCCESS) {
    let pawnId = getIdOfPawnWithMoves(action.fields);
    return action.pawns[pawnId].color;
  }

  return state;
}


export function time(state = 0, action) {
    switch (action.type) {
      case constants.INCREMENT_TIME:
        state++;
        if (state>40)state=0;
        return state;
      case constants.CLEAR_TIME:
        return 0;

    default:
      return state;
  }
}

export function gameStarted(state = false, action) {
  switch (action.type) {
    case constants.STATE_FETCH_SUCCESS:
      var initial_moves_string = "{\"1\":{\"position_after_move\":[4,2]},\"2\":{\"position_after_move\":[4,0]},\"3\":{\"position_after_move\":[4,4]},\"4\":{\"position_after_move\":[4,2]},\"5\":{\"position_after_move\":[4,6]},\"6\":{\"position_after_move\":[4,4]},\"7\":{\"position_after_move\":[4,6]}}";
      if(initial_moves_string !== JSON.stringify(action.moves)) {
        return true;
      }
      return false;

    default:
      return state;
  }
}
