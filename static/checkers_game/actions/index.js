import * as constatns from "../constants/action-types"
import { fetch as fetchPolyfill } from 'whatwg-fetch'

export function fetchBoardState(url, payload={}){
  console.log(url);
  return dispatch => {
    fetchPolyfill(url, {
      method:'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body:JSON.stringify(payload)
    })
    .then((response) => {
      if (!response.ok) throw Error(response.statusText);
      else return response;
    })
    .then((response) => response.json())
    .then((data) => normalizeData(data))
    .then((data) => dispatch(stateFetchSuccess(data)))
    .then(() => dispatch(playerTurn(false)))
    .catch((e) => {
      console.log(e);
      return dispatch(stateHasError(true));
    });
  }
}

function normalizeData(data){
  let pawns = data['white_pawns'].concat(data['black_pawns']);
  let statePart = {fields:{}, pawns:{}, moves:{}, winner:''};

  if(data['winner'] != undefined)statePart.winner = data['winner'];

  for (var i=0, moveId = 1; i<pawns.length; i++){
    if(!pawns[i])continue;
    let fieldKey = pawns[i].y + ' ' + pawns[i].x;
    let pawnId = i+1;

    let moves = pawns[i].moves != undefined ? pawns[i].moves : [];
    let pawnMovesId = [];
    for (let m = 0; m < moves.length; m++) {
      pawnMovesId.push(moveId);
      statePart.moves[moveId] = moves[m];
      moveId++;
    }
    pawns[i].moves = pawnMovesId;

    statePart.pawns[pawnId] = pawns[i];
    delete pawns[i].x
    delete pawns[i].y
    statePart.fields[fieldKey] = {'pawn':pawnId, 'fieldKey':fieldKey, 'moves':pawns[i].moves};
  }

  return statePart;
}

export function stateFetchSuccess(data){
  return {
    type:constatns.STATE_FETCH_SUCCESS,
    fields: data.fields,
    pawns: data.pawns,
    moves: data.moves,
    winner: data.winner
  }
}

export function stateHasError(bool){
  return {
    type:constatns.STATE_HAS_ERROR,
    hasError:bool
  }
}

export function playerTurn(bool){
  return {
    type:constatns.PLAYER_TURN,
    playerTurn:bool
  }
}