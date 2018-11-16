import React, {Component} from 'react';
import { connect } from 'react-redux';
import {fetch as fetchPolyfill} from 'whatwg-fetch';
import classnames from 'classnames';
import PropTypes from 'prop-types';

import { stateFetchSuccess, stateHasError, statePlayerTurn, fetchBoardState} from './actions/index.js'
import {pawnChoosed, choosePawn} from './actions/moves.js'

class Checkers extends Component{
  componentDidMount(){
    this.props.fetchBoardState('/move');
  }

  createFields(){
    let fields = [],
        id = 0;
    for (let y=0;y<8;y++){
      let row = [];
      for (let x=0;x<8;x++){
        id++;
        row = [...row, this.makeBoardField(x, y, id)];
      }
      fields = [...fields, row];
    }
    return fields;
  }

  makeBoardField(x, y, id){
    let color = (x+y)%2 == 0? 'white' : 'black';
    let fieldKey = y + ' ' + x;
    let field = this.props.fields[fieldKey] || null;

    if (!field) return FilerField(color, id);
    
    if(field.funcs) return ClickableField(color, id, field.funcs, this.props.pawns[field.pawn]);
    else return FilerField(color, id, this.props.pawns[field.pawn]);

  }

  render(){
    return (
      <div className='board'>
        {this.createFields()}
      </div>
    );
  }

}

const ClickableField = (color, id, funcs=null, pawn=null) => {
  let blockClass = 'board__field';
  return (
      <div
       className={classnames(blockClass, blockClass+'--'+color)}
       key={id}
       // onClick = {() => moveFun({'fieldKey': this.props.fieldKey, 'moves': this.props.pawnData.moves})}
       >
       {pawn ? Pawn(pawn) : null}
      </div>
    );
}

const FilerField = (color, id, pawn=null) => {
  let blockClass = 'board__field';
  return (
      <div
       className={classnames(blockClass, blockClass+'--'+color)}
       key={id}
       >
       {pawn ? Pawn(pawn) : null}
      </div>
    );
}

const Pawn = (props) => {
  let blockClass = 'pawn';
  return (
    <span
    className={classnames(blockClass, blockClass+'--'+props.color, blockClass+'--'+props.type)}
    >
    {props.id}
    </span>
  );
}

Checkers.propTypes = {
    fetchBoardState: PropTypes.func.isRequired,
    choosePawn: PropTypes.func.isRequired,
    hasError: PropTypes.bool.isRequired,
    playerTurn: PropTypes.bool.isRequired,
    pawnChoosed: PropTypes.object.isRequired,

    fields: PropTypes.object.isRequired,
    pawns: PropTypes.object.isRequired
};

const mapStateToProps = (state) => {
  return {
    fields: state.fields,
    pawns: state.pawns,
    moves: state.moves,
    hasError: state.stateHasError,
    playerTurn: state.statePlayerTurn,
    pawnChoosed: state.pawnChoosed
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    fetchBoardState: (url) => dispatch(fetchBoardState(url)),
    choosePawn: (pawnData) => dispatch(choosePawn(pawnData))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Checkers);

function isEmpty(obj) {
    for(var key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
}
