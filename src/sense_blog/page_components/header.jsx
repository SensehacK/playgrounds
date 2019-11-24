import React, { Component } from "react";
import { BrowserRouter as Router } from "react-router-dom";

class Header extends Component {
  state = {};
  render() {
    return (
      <Router>
        <header>
          <ul className="social">
            <li>
              <a href="/">Home</a>
            </li>
            <li>
              <a href="#/post1">Post1</a>
            </li>
            <li>
              <a href="#/post2">Post2</a>
            </li>
            <li>
              <a href="#/post3">Post3</a>
            </li>
          </ul>
        </header>
      </Router>
    );
  }
}

export default Header;
