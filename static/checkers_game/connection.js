import React, {Component} from 'react'
import {fetch as fetchPolyfill} from "whatwg-fetch"
import {connect} from 'react-redux'
import {fetchBoardState, playerTurn, connection, incrementTime, clearTime} from './actions/index'
import PropTypes from 'prop-types';
import classnames from 'classnames';


class Connection extends Component{

      constructor(props) {
        super(props);
      }

    componentDidMount() {
        var me = this;
        me.props.connection();
        setInterval(function () {
            if (me.props.gameStarted && me.props.winner === '') {
                me.props.incrementTime();
            }
        }, 1000);
    }

    makeTimer() {
          let timeLeft = 40 - this.props.time;
          return (
            <div>{timeLeft}</div>
          );
    }

    render() {
        let msg = this.props.joined == true? '' : 'waiting for other player';
        let cssClass = this.props.joined == true? '' : 'blink';
        if(this.props.joined == true){
            msg = this.props.playerTurn == true ? 'your turn' : 'other player turn';
        }
        return (
                <div className={classnames('blink--position', cssClass)}>
                    {msg}
                    <br/>
                    {this.makeTimer()}
                </div>
        );
    }
}

Connection.propTypes = {
    playerTurn: PropTypes.bool.isRequired,
    connection: PropTypes.func.isRequired,
    joined: PropTypes.bool.isRequired,
    gameStarted: PropTypes.bool.isRequired
}

const mapStateToProps = (state) => {
    return {
        playerTurn: state.statePlayerTurn,
        joined: state.joined,
        gameStarted: state.gameStarted,
        time: state.time,
        winner: state.winner
    }
}
const mapDispatchToProps = (dispatch) => {
    return {
        connection: () => dispatch(connection()),
        incrementTime: () => dispatch(incrementTime()),
        clearTime: () => dispatch(clearTime())
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Connection);
