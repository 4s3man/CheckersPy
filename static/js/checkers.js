import React, {Component} from 'react'
import classnames from 'classnames'

export default class Checkers extends Component{
  constructor(props, context){
    super(props);
    this.state = {
      fields: this.createFields()
    }
  }

  createFields(){
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
      <Coin id='1' position color='white' moves={[]} handler={this.coinHandler} />
    )
  }

  coinHandler(){
    alert('ok');
  }

  render(){
    return (
      <div className='board'>
        {this.state.fields}
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
const Coin = (id, color, position, moves, handler) => {
  let blockClass = 'coin';
  return (
    <span className={classnames(blockClass, blockClass+'--'+color)} />
  )
}
