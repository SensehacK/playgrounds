import React, { Component } from "react";
import SingularCounter from "./singularCounter";

class Counters extends Component {
  render() {
    console.log("Counters - Rendered");

    const { onReset, counters, onDelete, onIncrement } = this.props;

    // When the state is changed render Method is called again & so the updated state could be printed
    // console.log(" Counters printing in render component", this.state.counters);
    return (
      <div>
        {/* onReset={this.resetCounters} onIncrement={this.handleIncrement} onDelete={this.handleDelete} */}
        <button onClick={onReset} className="btn btn-primary btn-sm m-2">
          Reset
        </button>
        {counters.map(counter => (
          <SingularCounter
            key={counter.id}
            onIncrement={onIncrement}
            onDelete={onDelete}
            counter={counter}
            // id={counter.id}
          />
        ))}
      </div>
    );
  }
}

export default Counters;
