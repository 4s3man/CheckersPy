import * as constants from "../constants/action-types";

export function pawnChoosed(state = false, action){
  switch (action.type) {
    case constants.PAWN_CHOOSED:
      return action.clicked;

    default:
      return state;
  }
};
