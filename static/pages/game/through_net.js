//io attached in script above in layout.html
import "reset-css"
import "../shared_css/base.css"

import "./bundle_styles"
import {renderGame__withConnection} from "../../checkers_game/index.js"

renderGame__withConnection('/move_through_net', 'through_net');
