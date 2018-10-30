import React, {Component} from 'react'
import classnames from 'classnames'

export default class Checkers extends Component{
  constructor(props, context){
    super(props);
    this.s = {"white_pawns": [{"foreward": -1, "y": 5, "id": 0, "x": 1, "type": "normal", "color": "white"}, {"foreward": -1, "y": 5, "id": 1, "x": 3, "type": "normal", "color": "white"}, {"foreward": -1, "y": 5, "id": 2, "x": 5, "type": "normal", "color": "white"}, {"foreward": -1, "y": 5, "id": 3, "x": 7, "type": "normal", "color": "white"}, {"foreward": -1, "y": 6, "id": 4, "x": 0, "type": "normal", "color": "white"}, {"foreward": -1, "y": 6, "id": 5, "x": 2, "type": "normal", "color": "white"}, {"foreward": -1, "y": 6, "id": 6, "x": 4, "type": "normal", "color": "white"}, {"foreward": -1, "y": 6, "id": 7, "x": 6, "type": "normal", "color": "white"}, {"foreward": -1, "y": 7, "id": 8, "x": 1, "type": "normal", "color": "white"}, {"foreward": -1, "y": 7, "id": 9, "x": 3, "type": "normal", "color": "white"}, {"foreward": -1, "y": 7, "id": 10, "x": 5, "type": "normal", "color": "white"}, {"foreward": -1, "y": 7, "id": 11, "x": 7, "type": "normal", "color": "white"}], "black_pawns": [{"foreward": 1, "y": 0, "id": 0, "x": 0, "type": "normal", "color": "black"}, {"foreward": 1, "y": 0, "id": 1, "x": 2, "type": "normal", "color": "black"}, {"foreward": 1, "y": 0, "id": 2, "x": 4, "type": "normal", "color": "black"}, {"foreward": 1, "y": 0, "id": 3, "x": 6, "type": "normal", "color": "black"}, {"foreward": 1, "y": 1, "id": 4, "x": 1, "type": "normal", "color": "black"}, {"foreward": 1, "y": 1, "id": 5, "x": 3, "type": "normal", "color": "black"}, {"foreward": 1, "y": 1, "id": 6, "x": 5, "type": "normal", "color": "black"}, {"foreward": 1, "y": 1, "id": 7, "x": 7, "type": "normal", "color": "black"}, {"foreward": 1, "y": 2, "id": 8, "x": 0, "type": "normal", "color": "black"}, {"foreward": 1, "y": 2, "id": 9, "x": 2, "type": "normal", "color": "black"}, {"foreward": 1, "y": 2, "id": 10, "x": 4, "type": "normal", "color": "black"}, {"foreward": 1, "y": 2, "id": 11, "x": 6, "type": "normal", "color": "black"}]}
    this.state = {
      fields: this.createFields(this.createFieldsPawnObj()),
      playerTurn: true,
    }
  }

  createFieldsPawnObj(){
    let boardState = this.s['white_pawns'].concat(this.s['black_pawns']);
    let pawnFields = {}
    for (let i=0; i<boardState.length; i++){
      let key = boardState[i].x + ' ' + boardState[i].y;
      pawnFields[key] = Pawn(boardState[i]);
    }
    return pawnFields;
  }

  createFields(fieldPawn = null){
    let fields = [],
        id = 0;
    for (let y=0;y<8;y++){
      let row = [];
      for (let x=0;x<8;x++){
        id++;
        let color = (x+y)%2 == 0? 'white' : 'black';
        let pawn = fieldPawn[x + ' ' + y]? fieldPawn[x + ' ' + y] : null;
        row = [...row, <BoardField color={color} key={id} pawn={pawn}/>];
      }
      fields = [...fields, row];
    }
    return fields;
  }

  render(){
    return (
      <div className='board'>
        {this.state.fields}
      </div>
    );
  }
}

class BoardField extends Component{
  constructor(props, context){
    super(props, context);
  }
  render(){
    let blockClass = 'board__field';
    return (
      <div
       className={classnames(blockClass, blockClass+'--'+this.props.color)}
       key={this.props.id}
       >
       {this.props.pawn}
      </div>
    );
  }
}

// const BoardField = (color, key, pawn=null) => {
//     let blockClass = 'board__field';
//     return (
//       <div
//        className={classnames(blockClass, blockClass+'--'+color)}
//        key={key}
//        >
//        {pawn}
//       </div>
//     );
//   }
const Pawn = (props, handler) => {
  let blockClass = 'pawn';
  return (
    <span
    className={classnames(blockClass, blockClass+'--'+props.color)}
    onClick = {(e) => {props.handler()}}
    />
  )
}
