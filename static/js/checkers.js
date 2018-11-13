import React, {Component} from 'react';
import { connect } from 'react-redux';
import {fetch as fetchPolyfill} from 'whatwg-fetch';
import classnames from 'classnames';
import PropTypes from 'prop-types';

import { stateFetchSuccess, stateHasError, statePlayerTurn, fetchBoardState, pawnClicked } from './actions';

class Checkers extends Component{
  componentDidMount(){
    this.props.fetchBoardState('/move');
  }

  selectField() {
    console.log('ok');
  }

  make_move(moves){
    console.log(moves);
  }

  createFields(){
    let fieldPawn = this.dataToXYarray();
    let fields = [],
        id = 0;
    for (let y=0;y<8;y++){
      let row = [];
      for (let x=0;x<8;x++){
        id++;
        row = this.appendBoardField(x, y, id, row, fieldPawn)
      }
      fields = [...fields, row];
    }
    return fields;
  }

  appendBoardField(x, y, id, row, fieldPawn){
    let color = (x+y)%2 == 0? 'white' : 'black';
    let pawnData = fieldPawn && fieldPawn[x + ' ' + y]? fieldPawn[x + ' ' + y] : null;
    let shouldPulse = pawnData ? pawnData.moves.length != 0 : false;
    let pawn = pawnData ? Pawn(pawnData) : null;
    let boardField = <BoardField
                        pawn={pawn}
                        shouldPulse={shouldPulse}
                        color={color}
                        key={id}
                        selectField = {this.selectField}
                        />;

    return [...row, boardField];
  }

  dataToXYarray(){
    if (this.props.boardState['white_pawns'] == undefined) return null;
    let pawns = this.props.boardState['white_pawns'].concat(this.props.boardState['black_pawns']);
    let pawnFields = {}
    for (let i=0; i<pawns.length; i++){
      if (pawns[i]){
        let key = pawns[i].x + ' ' + pawns[i].y;
        pawnFields[key] = pawns[i];
      }
    }
    return pawnFields;
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
    let selectField = this.props.shouldPulse ? () => this.props.selectField() : () => {};
    return (
      <div
       className={classnames( {'board__field--pulse': this.props.shouldPulse}, blockClass, blockClass+'--'+this.props.color)}
       key={this.props.id}
       onClick = {selectField}
       >
       {this.props.pawn}
      </div>
    );
  }
}

const Pawn = (props) => {
  let blockClass = 'pawn';
  return (
    <span
    className={classnames(blockClass, blockClass+'--'+props.color, blockClass+'--'+props.type)}
    >
    {props.id}
    </span>
  )
}

Checkers.propTypes = {
    fetchBoardState: PropTypes.func.isRequired,
    boardState: PropTypes.object.isRequired,
    hasError: PropTypes.bool.isRequired,
    playerTurn: PropTypes.bool.isRequired,
    pawnClicked: PropTypes.bool.isRequired
};

const mapStateToProps = (state) => {
  return {
    boardState: state.stateFetchSuccess,
    hasError: state.stateHasError,
    playerTurn: state.statePlayerTurn,
    pawnClicked: state.pawnClicked
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    fetchBoardState: (url) => dispatch(fetchBoardState(url))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Checkers);
