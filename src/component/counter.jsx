import React, { Component } from "react";

class Counter extends Component {
  state = {
    count: 2,
    imgURL: "https://picsum.photos/250"
  };

  styles = {
    fontSize: 50,
    fontWeight: "bold"
  };

  //   <span className="badge badge-primary m-2">YO YO </span>
  //   <button className="btn btn-secondary btn-sm">Counter</button>

  render() {
    return (
      <React.Fragment>
        <h1>Hello Kautilya</h1>
        <button>Increment</button>
        <p> Count : {this.state.count}</p>
        <p>Addition {2 + 5}</p>
        <span> {this.formatCount()}</span>
        <div>
          <span> {this.formatCountJSXExpressions()}</span>
        </div>

        <h4>
          <span> Setting Attributes</span>
        </h4>
        <img src={this.state.imgURL} />

        <text> PAssing style object in expressions {"this.se"}</text>
        <p style={this.styles}> Img Random</p>

        <h5>Classes in React for Bootstrap CSs</h5>
        <span className="badge badge-primary m-2">YO YO </span>
        <button className="btn btn-secondary btn-sm">Counter</button>

        <p style={{ fontSize: 30 }}> Font size : 30</p>

        <h5> Conditional CSS properties</h5>
        <span className={this.getButtonColor()}>YO YO </span>
        <button className="btn btn-secondary btn-sm">Counter</button>
      </React.Fragment>
    );
  }

  getButtonColor() {
    let classes = "badge m-2 badge-";
    classes += this.state.count === 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    return this.state.count === 0 ? "Zero" : this.state.count;
  }

  formatCountJSXExpressions() {
    const { count } = this.state;
    return count === 5 ? <h1>Hell Sense {count}</h1> : count;
  }
}

export default Counter;
