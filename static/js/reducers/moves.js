import * as constants from "../constants/action-types";

export function pawnChoosed(state = {}, action){
  switch (action.type) {
    case constants.PAWN_CHOOSED:
      return action.choosenPawn;

    default:
      return state;
  }
};
