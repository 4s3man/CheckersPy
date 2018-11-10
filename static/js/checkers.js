import React, {Component} from 'react';
import { connect } from 'react-redux';
import {fetch as fetchPolyfill} from 'whatwg-fetch';
import classnames from 'classnames';
import PropTypes from 'prop-types';

import { stateFetchSuccess, stateHasError, statePlayerTurn, fetchBoardState } from './actions';

class Checkers extends Component{
  componentDidMount(){
    this.props.fetchBoardState('/move');
  }

  createFieldsPawnObj(){
    if (this.props.boardState['white_pawns'] == undefined) return null;
    let pawns = this.props.boardState['white_pawns'].concat(this.props.boardState['black_pawns']);
    let pawnFields = {}
    for (let i=0; i<pawns.length; i++){
      if (pawns[i]){
        let key = pawns[i].x + ' ' + pawns[i].y;
        pawnFields[key] = Pawn(pawns[i]);
      }
    }
    return pawnFields;
  }

  createFields(){
    let fieldPawn = this.createFieldsPawnObj();
    let fields = [],
        id = 0;
    for (let y=0;y<8;y++){
      let row = [];
      for (let x=0;x<8;x++){
        id++;
        let color = (x+y)%2 == 0? 'white' : 'black';
        let pawn = fieldPawn && fieldPawn[x + ' ' + y]? fieldPawn[x + ' ' + y] : null;
        row = [...row, <BoardField color={color} key={id} pawn={pawn}/>];
      }
      fields = [...fields, row];
    }
    return fields;
  }

  render(){
    return (
      <div className='board'>
        {this.createFields()}
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

const Pawn = (props, handler) => {
  let blockClass = 'pawn';
  return (
    <span
    className={classnames(blockClass, blockClass+'--'+props.color)}
    onClick = {(e) => {props.handler()}}
    >
    {props.id}
    </span>
  )
}

Checkers.propTypes = {
    fetchBoardState: PropTypes.func.isRequired,
    boardState: PropTypes.object.isRequired,
    hasError: PropTypes.bool.isRequired,
    playerTurn: PropTypes.bool.isRequired
};

const mapStateToProps = (state) => {
  return {
    boardState: state.stateFetchSuccess,
    hasError: state.stateHasError,
    playerTurn: state.statePlayerTurn
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    fetchBoardState: (url) => dispatch(fetchBoardState(url))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Checkers);
