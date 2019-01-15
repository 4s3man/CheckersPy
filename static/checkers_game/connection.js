import React, {Component} from 'react'
import {fetch as fetchPolyfill} from "whatwg-fetch"
import {connect} from 'react-redux'
import {connectionPlayerTurn} from './actions/index'
import {statePlayerTurn} from "./reducers/board-state";
import PropTypes from 'prop-types';

class Connection extends Component{

    // #todo ma ściągać rid i pid do sprawdzania czyja kolej i jesli jego to odblokowywać fetchMove w checkers
    componentWillMount() {
        // this.init_connection();
    }

    componentDidMount() {
        this.props.dispatchPlayerTurn('/through_net_connection', 'get_turn');
        // this.timer = setInterval(this.fetch_rooms.bind(this), 1000);
    }

    componentWillUnmount() {
        // clearInterval(this.timer);
    }

    init_connection() {
        // fetchPolyfill('/through_net_connection', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify('init')
        // })
        //     .then((response) => {
        //         if (!response.ok) throw Error(response.statusText);
        //         else return response;
        //     })
        //     .then((response) => response.json())
    }

    fetch_rooms(){
        fetchPolyfill('/through_net_connection', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body:JSON.stringify('')
        })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          else return response;
        })
        .then((response) => response.json())
        .then((data)=>{
            if(data['room_error'] != undefined){
                window.location.assign(data['room_error']);
            }
            if (data['turn'] != undefined){
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
        dispatchPlayerTurn: (url, payload) => dispatch(connectionPlayerTurn(url, payload))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Connection);
