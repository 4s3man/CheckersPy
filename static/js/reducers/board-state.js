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

export function fields(state = {}, action){
  switch (action.type) {
    case constants.STATE_FETCH_SUCCESS:
      return action.fields;

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
