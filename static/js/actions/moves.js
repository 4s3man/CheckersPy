import * as constants from "../constants/action-types";

export function updateFieldFunc(fieldMoveObj){
  return {
    type:constants.SELECT_FIELD_FUNCTIONS_UPDATE,
    field: fieldMoveObj.fieldKey,
    normalizedMoves: fieldMoveObj.moves
  }
}

export function deselectFieldFunc(){
  return {
    type:constants.DESELECT_FIELD_FUNCTIONS_UPDATE
  }
}

export function selectPawn(payload){
    return (dispatch, getState) => {
      dispatch(
        updateFieldFunc(
          normalizePayloadMoves(getState, payload)
        )
      );
    }
}

export function deselectPawn(payload){
    return (dispatch) => {
      dispatch(deselectFieldFunc());
    }
}

function normalizePayloadMoves(getState, payloadSrc){
  let payload = Object.assign({}, payloadSrc);
  let state = getState();
  let beatedPawnColor = state.pawns[state.fields[payload['fieldKey']].pawn].color === 'white' ?
    'black' : 'white';
  let movesIds = payload['moves'];
  let moves = movesIds.map((id)=>state.moves[id]);

  payload.moves = moves.map((move) => {
    let preparedMove = {'position_after_move':'', 'beated_pawn_ids':[]};

    if(move.position_after_move)
      preparedMove.position_after_move = move.position_after_move.join(' ');

    if(move.beated_pawn_ids){
      preparedMove.beated_pawn_ids = move.beated_pawn_ids.map((id)=>{
        let pawns = state.pawns;
        for (let key in pawns)
          if (pawns.hasOwnProperty(key) && pawns[key].id === id && pawns[key].color == beatedPawnColor)
              return key;
      });
    }

    return preparedMove;
  });

  return payload;
}
