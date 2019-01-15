import React, {Component} from 'react';
import { connect } from 'react-redux';
import {fetch as fetchPolyfill} from 'whatwg-fetch';
import classnames from 'classnames';
import PropTypes from 'prop-types';
import CheckersCtrl from './checkersCtrl'

import { stateFetchSuccess, stateHasError, statePlayerTurn, winner, fetchBoardState} from './actions/index.js'
import {deselectPawn, selectPawn} from './actions/moves.js'

class Checkers extends Component{
  constructor(props) {
   super(props);
   this.moveUrl = this.props.moveUrl || '';
   this.through_net = this.props.through_net || false;
   if ('' === this.moveUrl)console.log('Missing moveUrl in Checkers. Please provide valid one.');
  }
  componentDidMount(){
      this.props.fetchBoardState(this.moveUrl);
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
    let pawn = this.props.pawns[field.pawn] || null;

    if(field.funcs && this.through_net && this.props.playerTurn == false){
      return FilerField(color, id, pawn);
    }

    if(field.funcs && !this.props.winner){
      let fieldFunc = null;
      let pawn = this.props.pawns[field.pawn]
      switch (field.funcs) {
        case 'deselectPawn':
          fieldFunc = () => this.props.deselectPawn();
          break;
        case 'fetchBoardState':
          fieldFunc = () => this.props.fetchBoardState(this.moveUrl, this.props.moveDataTmp[fieldKey]);
          break;
        default:
          fieldFunc = () => this.props.selectPawn({'fieldKey':fieldKey, 'moves':pawn.moves});
      }
      return ClickableField(color, id, field, fieldFunc, pawn);
    }
    else return FilerField(color, id, pawn);
  }

  makeDialogWindow(){
    if(this.props.winner)return GameEndWindow(this.props.winner, this.props.actionSufix);
  }

  render(){
    return (
      <div className='game_board board'>
        {this.makeDialogWindow()}
        {this.createFields()}
      </div>
    );
  }

}

const ClickableField = (color, id, field, func, pawn=null) => {
  let blockClass = 'board__field';
  let pulse = field.funcs ? 'pulse--' + field.funcs : '';
  return (
      <div
       className={classnames(pulse, blockClass, blockClass+'--'+color)}
       key={id}
       onClick = {() => func()}
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

const GameEndWindow = (winner, actionSuffix='') => {
  let text = winner == 'draw' ? winner + '!': winner + ' wins!';
  return (
    <div className='dialogWindow dialogWindow--success'>
        <div className='dialogWindow__info'>
          <h4 className='dialogWindow__title'>{text}</h4>
        </div>
      <nav className='dialogWindow__nav'>
        <CheckersCtrl actionSufix={actionSuffix}/>
      </nav>
    </div>
  );
}

Checkers.propTypes = {
    fetchBoardState: PropTypes.func.isRequired,
    selectPawn: PropTypes.func.isRequired,
    hasError: PropTypes.bool.isRequired,
    playerTurn: PropTypes.bool.isRequired,

    fields: PropTypes.object.isRequired,
    pawns: PropTypes.object.isRequired,
    moveDataTmp: PropTypes.object.isRequired,
};

const mapStateToProps = (state) => {
  return {
    fields: state.fields,
    pawns: state.pawns,
    moves: state.moves,
    winner: state.winner,
    hasError: state.stateHasError,
    playerTurn: state.statePlayerTurn,
    moveDataTmp: state.moveDataTmp
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    fetchBoardState: (url, payload={}) => dispatch(fetchBoardState(url, payload)),
    selectPawn: (moves) => dispatch(selectPawn(moves)),
    deselectPawn: () => dispatch(deselectPawn())
  };
}
export default connect(mapStateToProps, mapDispatchToProps)(Checkers);
