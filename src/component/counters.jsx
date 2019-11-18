import React, { Component } from "react";
import SingularCounter from "./singularCounter";

class Counters extends Component {
  render() {
    // When the state is changed render Method is called again & so the updated state could be printed
    // console.log(" Counters printing in render component", this.state.counters);
    return (
      <div>
        {/* onReset={this.resetCounters} onIncrement={this.handleIncrement} onDelete={this.handleDelete} */}
        <button
          onClick={this.props.onReset}
          className="btn btn-primary btn-sm m-2"
        >
          Reset
        </button>
        {this.props.counters.map(counter => (
          <SingularCounter
            key={counter.id}
            onIncrement={this.props.onIncrement}
            onDelete={this.props.onDelete}
            counter={counter}
            // id={counter.id}
          />
        ))}
      </div>
    );
  }
}

export default Counters;
