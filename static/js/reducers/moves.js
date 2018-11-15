import * as constants from "../constants/action-types";

export function pawnClicked(state = false, action){
  switch (action.type) {
    case constants.PAWN_CLICKED:
      return action.clicked;

    default:
      return state;
  }
};
