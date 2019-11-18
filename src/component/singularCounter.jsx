import React, { Component } from "react";

class SingularCounter extends Component {
  state = {
    value: this.props.value ? this.props.value : 0 // Setting counter value via props
  };

  render() {
    console.log(this.props);

    return (
      <div>
        <h3>Counter #{this.props.id}</h3>
        <span className="badge badge-primary m-2">{this.state.value} </span>
        <button
          className="btn btn-secondary btn-sm"
          onClick={this.handleIncrement}
        >
          Counter
        </button>
        <button
          onClick={() => this.props.onDelete(this.props.id)}
          className="btn btn-danger btn-sm m-2"
        >
          Delete
        </button>
      </div>
    );
  }

  handleIncrement = () => {
    // Updating the state
    this.setState({ value: this.state.value + 1 });
  };
}

export default SingularCounter;
