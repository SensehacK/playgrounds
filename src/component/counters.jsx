import React, { Component } from "react";
import Counter from "./counter";
import SingularCounter from "./singularCounter";

class Counters extends Component {
  state = {
    counters: [
      { id: 1, value: 0 },
      { id: 2, value: 3 },
      { id: 3, value: 2 },
      { id: 4, value: 3 }
    ]
  };

  handleDelete = counterID => {
    console.log("Delete func called", counterID);
    const counters = this.state.counters.filter(c => c.id != counterID);
    // this.state.counters = counters; We can set state like this, React won't notice the change management like angular
    this.setState({ counters: counters }); // Simplify setState ({counters}) As both are same, destructive construction object something
  };

  render() {
    return (
      <div>
        {this.state.counters.map(counter => (
          <SingularCounter
            key={counter.id}
            onDelete={this.handleDelete}
            value={counter.value}
            id={counter.id}
          />
        ))}
      </div>
    );
  }
}

export default Counters;
