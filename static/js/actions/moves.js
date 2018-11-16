import * as constants from "../constants/action-types";

export function pawnChoosed(moves){
  return {
    type:constants.PAWN_CHOOSED,
    choosenPawn:moves
  }
}

export function choosePawn(moves){
  return (dispatch) => {
    console.log(moves);  
    dispatch(pawnChoosed(moves));
  }
}
