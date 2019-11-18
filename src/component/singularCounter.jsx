import React, { Component } from "react";

class SingularCounter extends Component {
  // state = {
  //   value: this.props.counter.value ? this.props.counter.value : 0 // Setting counter value via props
  // };

  render() {
    // console.log("Render function called");

    // console.log(this.props);

    return (
      <div>
        <h3>Counter #{this.props.counter.id}</h3>
        <span className={this.getBadgeClasses()}>{this.formatCount()}</span>
        <button
          className="btn btn-secondary btn-sm"
          onClick={() => this.props.onIncrement(this.props.counter)}
        >
          Counter
        </button>
        <button
          onClick={() => this.props.onDelete(this.props.counter.id)}
          className="btn btn-danger btn-sm m-2"
        >
          Delete
        </button>
      </div>
    );
  }

  getBadgeClasses() {
    let classes = "badge m-2 badge-";
    classes += this.props.counter.value === 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    const { value } = this.props.counter;
    return value === 0 ? "Zero" : value;
  }
}

export default SingularCounter;
