import React, {Component} from 'react'
import {fetch as fetchPolyfill} from "whatwg-fetch"

export default class ActiveRooms extends Component{
    constructor(){
        super();
        this.state = {
            'rooms_number': 0
        }
    }

    componentWillMount() {
        this.fetch_rooms();
    }

    componentDidMount() {
        this.timer = setInterval(this.fetch_rooms.bind(this), 1000);
    }

    componentWillUnmount() {
        clearInterval(this.timer);
    }

    fetch_rooms(){
        fetchPolyfill('/16_kulaga/checkerspy/fetch_rooms', {
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
            this.setState({'rooms_number': data});
        });
    }

    render() {
        return (
                this.state.rooms_number
        );
    }
}
