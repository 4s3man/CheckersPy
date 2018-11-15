import * as constatns from "../constants/action-types"
import { fetch as fetchPolyfill } from 'whatwg-fetch'

export function fetchBoardState(url){
  return dispatch => {
    dispatch(playerTurn(false));
    
    fetchPolyfill(url, {method:'POST'})
    .then((response) => {
      if (!response.ok) throw Error(response.statusText);
      else return response;
    })
    .then((response) => response.json())
    .then((data) => dispatch(stateFetchSuccess(data)))
    .then(() => dispatch(playerTurn(true)))
    .catch((e) => {
      console.log(e);
      return dispatch(stateHasError(true));
    });
  }
}


export function stateFetchSuccess(state){
  return {
    type:constatns.STATE_FETCH_SUCCESS,
    state
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
