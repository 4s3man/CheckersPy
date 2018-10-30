import React, {Component} from 'react'
import classnames from 'classnames'

export default class Checkers extends Component{
  constructor(props, context){
    super(props);
    this.state = {
      fields: this.createFields(),
      boardState: {"white_pawns": [{"foreward": -1, "y": 5, "id": 0, "x": 1, "type": "normal", "color": "white"}, {"foreward": -1, "y": 5, "id": 1, "x": 3, "type": "normal", "color": "white"}, {"foreward": -1, "y": 5, "id": 2, "x": 5, "type": "normal", "color": "white"}, {"foreward": -1, "y": 5, "id": 3, "x": 7, "type": "normal", "color": "white"}, {"foreward": -1, "y": 6, "id": 4, "x": 0, "type": "normal", "color": "white"}, {"foreward": -1, "y": 6, "id": 5, "x": 2, "type": "normal", "color": "white"}, {"foreward": -1, "y": 6, "id": 6, "x": 4, "type": "normal", "color": "white"}, {"foreward": -1, "y": 6, "id": 7, "x": 6, "type": "normal", "color": "white"}, {"foreward": -1, "y": 7, "id": 8, "x": 1, "type": "normal", "color": "white"}, {"foreward": -1, "y": 7, "id": 9, "x": 3, "type": "normal", "color": "white"}, {"foreward": -1, "y": 7, "id": 10, "x": 5, "type": "normal", "color": "white"}, {"foreward": -1, "y": 7, "id": 11, "x": 7, "type": "normal", "color": "white"}], "black_pawns": [{"foreward": 1, "y": 0, "id": 0, "x": 0, "type": "normal", "color": "black"}, {"foreward": 1, "y": 0, "id": 1, "x": 2, "type": "normal", "color": "black"}, {"foreward": 1, "y": 0, "id": 2, "x": 4, "type": "normal", "color": "black"}, {"foreward": 1, "y": 0, "id": 3, "x": 6, "type": "normal", "color": "black"}, {"foreward": 1, "y": 1, "id": 4, "x": 1, "type": "normal", "color": "black"}, {"foreward": 1, "y": 1, "id": 5, "x": 3, "type": "normal", "color": "black"}, {"foreward": 1, "y": 1, "id": 6, "x": 5, "type": "normal", "color": "black"}, {"foreward": 1, "y": 1, "id": 7, "x": 7, "type": "normal", "color": "black"}, {"foreward": 1, "y": 2, "id": 8, "x": 0, "type": "normal", "color": "black"}, {"foreward": 1, "y": 2, "id": 9, "x": 2, "type": "normal", "color": "black"}, {"foreward": 1, "y": 2, "id": 10, "x": 4, "type": "normal", "color": "black"}, {"foreward": 1, "y": 2, "id": 11, "x": 6, "type": "normal", "color": "black"}]}
    }
    console.log(this.state.fields[0][0]);
  }

  createFields(boardState = null){
    let fields = [],
        id = 0,
        color = null;
    for (let y=0;y<8;y++){
      let row = [];
      for (let x=0;x<8;x++){
        id++;
        color = (x+y)%2 == 0? 'white' : 'black';
        row = [...row, BoardField(color, id)];
      }
      fields = [...fields, row];
    }
    return fields;
  }

  getCoin(){
    return (
      <Coin props={{"foreward": 1, "y": 0, "id": 0, "x": 0, "type": "normal", "color": "black"}} handler={this.coinHandler} />
    )
  }

  coinHandler(){
    alert('ok');
  }

  render(){
    return (
      <div className='board'>
        {this.state.fields}
        {this.getCoin()}
      </div>
    );
  }
}
const BoardField = (color, key, coin=null) => {
    let blockClass = 'board__field';
    return (
      <div
       className={classnames(blockClass, blockClass+'--'+color)}
       key={key}
       >
       {coin}
      </div>
    );
  }
const Coin = (props, handler) => {
  let blockClass = 'coin';
  console.log(props);
  return (
    <span
    className={classnames(blockClass, blockClass+'--'+props.props.color)}
    onClick = {(e) => {props.handler()}}
    />
  )
}
