import React, {Component} from 'react'
import {fetch as fetchPolyfill} from "whatwg-fetch"
import {connect} from 'react-redux'
import {fetchBoardState, playerTurn, connection} from './actions/index'
import PropTypes from 'prop-types';
import classnames from 'classnames';


class Connection extends Component{

    componentDidMount() {
        this.props.connection();
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
                    {/*todo time for move*/}
                </div>
        );
    }
}

Connection.propTypes = {
    playerTurn: PropTypes.bool.isRequired,
    connection: PropTypes.func.isRequired,
    joined: PropTypes.bool.isRequired,
    // time: PropTypes.int.isRequired
}

const mapStateToProps = (state) => {
    return {
        playerTurn: state.statePlayerTurn,
        joined: state.joined,
        time: state.time
    }
}
const mapDispatchToProps = (dispatch) => {
    return {
        connection: () => dispatch(connection()),
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Connection);
