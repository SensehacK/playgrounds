import React, { Component } from "react";

class SingularCounter extends Component {
  state = {
    count: 2,
    imgURL: "https://picsum.photos/250",
    tags: ["tag1", "tag2", "tag3"]
  };

  render() {
    return (
      <React.Fragment>
        <h1>Hello Kautilya</h1>

        <h3>Increment Counters and properly set data</h3>
        <span className="badge badge-primary m-2">{this.state.count} </span>
        <button
          className="btn btn-secondary btn-sm"
          onClick={this.handleIncrement}
        >
          Counter+1
        </button>
      </React.Fragment>
    );
  }

  handleIncrement = () => {
    console.log("Hi in func increment");
    // Updating the state
    this.setState({ count: this.state.count + 1 });
  };
}

export default SingularCounter;
