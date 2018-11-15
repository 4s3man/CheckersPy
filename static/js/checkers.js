import React, {Component} from 'react';
import { connect } from 'react-redux';
import {fetch as fetchPolyfill} from 'whatwg-fetch';
import classnames from 'classnames';
import PropTypes from 'prop-types';

import { stateFetchSuccess, stateHasError, statePlayerTurn, fetchBoardState, pawnChoosed, chooseMove } from './actions';

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
    let fieldsData = this.props.fieldsData;
    if (isEmpty(fieldsData)) return <BoardField color={color} key={id} /> ;

    let fieldKey = y + ' ' + x;
    let fieldData = fieldsData[fieldKey] != undefined ? fieldsData[fieldKey] : null;
    let pawnData = fieldData && fieldData.pawn != undefined ? fieldData.pawn : null;

    return <BoardField
                        pawnData={pawnData}
                        color={color}
                        key={id}
                        />;
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
  render(){
    let blockClass = 'board__field';
    let pawn = this.props.pawnData ? Pawn(this.props.pawnData) : null;
    let shouldPulse = pawn && this.props.pawnData.moves != undefined ? this.props.pawnData.moves.length != 0 : null;

    return (
      <div
       className={classnames( {'board__field--pulse': shouldPulse}, blockClass, blockClass+'--'+this.props.color)}
       key={this.props.id}
       >
       {pawn}
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
    chooseMove: PropTypes.func.isRequired,
    fieldsData: PropTypes.object.isRequired,

    hasError: PropTypes.bool.isRequired,
    playerTurn: PropTypes.bool.isRequired,
    pawnChoosed: PropTypes.bool.isRequired
};

const mapStateToProps = (state) => {
  return {
    fieldsData: state.stateFetchSuccess,
    hasError: state.stateHasError,
    playerTurn: state.statePlayerTurn,
    pawnChoosed: state.pawnChoosed
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    fetchBoardState: (url) => dispatch(fetchBoardState(url)),
    chooseMove: (move) => dispatch(chooseMove(move))
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
