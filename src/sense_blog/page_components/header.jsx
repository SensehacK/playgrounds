import React, { Component } from "react";
import { BrowserRouter as Router, Link } from "react-router-dom";

class Header extends Component {
  state = {};
  render() {
    return (
      <header>
        <ul className="social">
          <Router>
            <li>{/* <Link to={"/"}>Home</Link> */}</li>
          </Router>
        </ul>
      </header>
    );
  }
}

export default Header;
