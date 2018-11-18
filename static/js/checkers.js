import React, {Component} from 'react';
import { connect } from 'react-redux';
import {fetch as fetchPolyfill} from 'whatwg-fetch';
import classnames from 'classnames';
import PropTypes from 'prop-types';

import { stateFetchSuccess, stateHasError, statePlayerTurn, fetchBoardState} from './actions/index.js'
import {deselectPawn, selectPawn} from './actions/moves.js'

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

    if(field.funcs){
      let fieldFunc = null;
      switch (field.funcs) {
        case 'deselectPawn':
          fieldFunc = () => this.props.deselectPawn();
          break;
        case 'fetchBoardState':
          fieldFunc = () => this.props.fetchBoardState('/move', {'stuff':'dono'});
          break;
        default:
          fieldFunc = () => this.props.selectPawn({'fieldKey':fieldKey, 'moves':this.props.pawns[field.pawn].moves});
      }
      return ClickableField(color, id, field, fieldFunc, this.props.pawns[field.pawn]);
    }
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

Checkers.propTypes = {
    fetchBoardState: PropTypes.func.isRequired,
    selectPawn: PropTypes.func.isRequired,
    hasError: PropTypes.bool.isRequired,
    playerTurn: PropTypes.bool.isRequired,

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
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    fetchBoardState: (url) => dispatch(fetchBoardState(url)),
    selectPawn: (moves) => dispatch(selectPawn(moves)),
    deselectPawn: () => dispatch(deselectPawn())
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Checkers);
