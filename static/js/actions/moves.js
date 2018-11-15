import * as constants from "../constants/action-types";

export function pawnChoosed(bool){
  return {
    type:constants.PAWN_CHOOSED,
    clicked:bool
  }
}

export function choosePawn(){
  return dispatch => {
    console.log('ok');
    dispatch(pawnChoosed(true));
  }
}
