import React, { Component } from "react";
import { BrowserRouter as Router, Link } from "react-router-dom";
// TODO:
class Header extends Component {
  state = {};
  render() {
    return (
      <Router>
        <header>
          <ul className="social">
            {/* Couldn't figure this out */}
            {/* Link doesn't route properly but a href does */}
            <li>
              <Link to="/">!Home</Link>
            </li>
            <li>
              <a href="/">Home</a>
            </li>
            <li>
              <Link to="/post2">!Post</Link>
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
