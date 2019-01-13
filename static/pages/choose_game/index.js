//io attached in script above in layout.html
import "./bundle_styles.js"
import React from 'react'
import {render} from 'react-dom'
import ActiveRooms from "./activeRooms"

render(
    <ActiveRooms/>,
    document.getElementById('JS-activeRooms')
);
