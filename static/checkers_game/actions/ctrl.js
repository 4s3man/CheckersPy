import * as constatns from "../constants/action-types"
import { fetch as fetchPolyfill } from 'whatwg-fetch'

export function ctrlLeave(url, payload={}){
  return dispatch => {

    fetchPolyfill(url, {
      method:'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body:JSON.stringify(payload)
    });
    // .then((response) => {
    //   if (!response.ok) throw Error(response.statusText);
    //   else return response;
    // })
    // .then((response) => response.json())
    // .then((data) => normalizeData(data))
    // .then((data) => dispatch(stateFetchSuccess(data)))
    // .catch((e) => {
    //   console.log(e);
    // });
  }
}
