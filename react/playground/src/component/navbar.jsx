import React, { Component } from "react";

// Stateless function can't have Class lifecycle hooks
const NavBar = ({ totalCounters }) => {
  console.log("NavBar - Rendered");

  return (
    <nav className="navbar navbar-light bg-light">
      <a className="navbar-brand" href="#">
        Navbar{" "}
        <span className="badbe badge-pill badge-secondary">
          {totalCounters}
        </span>
      </a>
    </nav>
  );
};

export default NavBar;
