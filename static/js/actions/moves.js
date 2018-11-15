import * as constants from "../constants/action-types";

export function pawnChoosed(bool){
  return {
    type:constatns.PAWN_CLICKED,
    clicked:bool
  }
}

export function choosePawn(move){
  return dispatch => {
    console.log('ok');
    dispatch(pawnClicked(true));
  }
}

export function makeMove(move){

}
