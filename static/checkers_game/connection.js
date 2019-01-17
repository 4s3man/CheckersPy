import React, {Component} from 'react'
import {fetch as fetchPolyfill} from "whatwg-fetch"
import {connect} from 'react-redux'
import {fetchBoardState, playerTurn, connection} from './actions/index'
import PropTypes from 'prop-types';

class Connection extends Component{

    componentDidMount() {
        this.props.connection();
    }

    render() {
        let msg = this.props.joined == true? '' : 'waiting for other player';
        let cssClass = this.props.joined == true? '' : 'blink';
        msg = this.props.playerTurn == true ? 'your turn' : 'otherg player turn';
        return (
                <div className={cssClass}>
                    {msg}
                </div>
        );
    }
}

Connection.propTypes = {
    playerTurn: PropTypes.bool.isRequired,
    connection: PropTypes.func.isRequired,
    joined: PropTypes.bool.isRequired
}

const mapStateToProps = (state) => {
    return {
        playerTurn: state.statePlayerTurn,
        joined: state.joined
    }
}
const mapDispatchToProps = (dispatch) => {
    return {
        connection: () => dispatch(connection()),
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Connection);
