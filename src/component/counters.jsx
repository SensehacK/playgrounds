import React, { Component } from "react";
import Counter from "./counter";
import SingularCounter from "./singularCounter";

class Counters extends Component {
  state = {};
  render() {
    return (
      //   <div>
      //     <Counter />
      //     <Counter />
      //     <Counter />
      //     <Counter />
      //   </div>

      <div>
        <SingularCounter />
        <SingularCounter />
        <SingularCounter />
      </div>
    );
  }
}

export default Counters;
