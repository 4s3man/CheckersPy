import React from "react";
import {render} from 'react-dom'
import Slider from "react-slick";

import "reset-css"
import "../shared_css/base.css"
import "./history.css"

class SimpleSlider extends React.Component {

  constructor(props) {
   super(props);
   this.url = "/static/images/"
   this.slides = [
     {
       "title":"name"
     }
   ];
  }

  componentDidMount() {
    document.getElementsByClassName('slide')[0].focus();
  }

  createImage(img, alt, title, description) {
    let url = this.url + img;

    return ( <div className="slide">
              <div className="slide__textBox">
                <h3 className="slide__title title t2">{title}</h3>
                <p className="p">{description}</p>
              </div>
              <img className="slide__img" src={url} alt={alt}/>
            </div>
          );
  }

  render() {
    var settings = {
      dots: true,
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      slidesToScroll: 1,
      accessibility: true
    };

    return (
      <Slider {...settings}>
        {this.createImage(
          "senet.jpeg",
          "Senet",
          'the beginings',
          'Board games were invented over thousands of years ago, noone knows when exactly.\
          One of the first games was Egyptian Senet, invented over 3000 years BC.'
        )}
      {this.createImage(
        "petteia.jpeg",
        "petteia",
        'grece',
        'In ancient Grece people were playing in Petteia.'
      )}
      {this.createImage(
        "latrunculi.jpg",
        "Latrunculi",
        'rome',
        'Due to the Romans awkward manner to steal things from Greeks, they stolen also Petteia. \
        Wchich was later on transformed to game called Latrunculi.'
      )}
      {this.createImage(
        "middleAgesCheckers.jpg",
        "middleAgesCheckers",
        'Checkers as we know',
        'Nowadays checkers were invented in the Middle Ages on the south of Europe.'
      )}
      {this.createImage(
        "france.jpeg",
        "france checkers",
        'Black and white checquer',
        'In france first time the black and white checquer was used.'
      )}
      </Slider>
    );
  }
}

render(<SimpleSlider/>, document.getElementById('JS-slider'));
