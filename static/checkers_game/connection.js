import React, {Component} from 'react'
import {fetch as fetchPolyfill} from "whatwg-fetch"
import {connect} from 'react-redux'
import {fetchBoardState, playerTurn} from './actions/index'
import PropTypes from 'prop-types';

class Connection extends Component{

    componentDidMount() {
        if (this.props.playerTurn == false) {
            this.timer = setInterval(this.fetch_rooms.bind(this), 1000);
        }else{
            this.props.fetchBoardState('move_through_net', {});
            clearInterval(this.timer);
        }
    }

    componentWillUnmount() {
        clearInterval(this.timer);
    }

    fetch_rooms(){
        fetchPolyfill('/through_net_connection', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify('')
        })
            .then((response) => {
                if (!response.ok) throw Error(response.statusText);
                else return response;
            })
            .then((response) => response.json())
            .then((data) => {
                if (data['room_error'] != undefined) {
                    window.location.assign(data['room_error']);
                }
                if (data['playerTurn'] != undefined && data['joined'] == true) {
                    this.props.setPlayerTurn(data['playerTurn']);
                    if(this.props.playerTurn == true){
                        this.props.fetchBoardState('move_through_net', {});
                    }
                }
            });
    }

    render() {
        return (
                <div>
                    ok
                </div>
        );
    }
}

Connection.propTypes = {
    playerTurn: PropTypes.bool.isRequired,
}

const mapStateToProps = (state) => {
    return {
        playerTurn: state.statePlayerTurn,
    }
}
const mapDispatchToProps = (dispatch) => {
    return {
        setPlayerTurn: (bool) => dispatch(playerTurn(bool)),
        fetchBoardState: (url, payload) => dispatch(fetchBoardState((url, payload)))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Connection);
