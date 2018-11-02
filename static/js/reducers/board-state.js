import * as constants from "../constants/action-types";

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
      return action.state;

    default:
      return state;
  }
};
