import React, { Component } from "react";

class Counter extends Component {
  state = {
    count: 2,
    imgURL: "https://picsum.photos/250",
    // tags: []
    tags: ["tag1", "tag2", "tag3"]
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
        <img src={this.state.imgURL} alt="Random Img Sum" />
        <p> PAssing style object in expressions {"this.se"}</p>
        <p style={this.styles}> Img Random</p>
        <h5>Classes in React for Bootstrap CSs</h5>
        <span className="badge badge-primary m-2">YO YO </span>
        <button className="btn btn-secondary btn-sm">Counter</button>
        <p style={{ fontSize: 30 }}> Font size : 30</p>
        <h5> Conditional CSS properties</h5>
        <span className={this.getButtonColor()}>YO YO </span>
        <button className="btn btn-secondary btn-sm">Counter</button>
        <ul>
          {this.state.tags.map(tag => (
            <li key={tag}> {tag} </li>
          ))}
        </ul>
        <p> One more refactored array method</p>
        {this.state.tags.length === 0 && "Please enter the array tags"}
        {this.renderTagsArr()}

        <h3>Increment Counters and properly set data</h3>
        <span className="badge badge-primary m-2">{this.state.count} </span>
        <button
          className="btn btn-secondary btn-sm"
          onClick={this.handleIncrement}
        >
          Counter+1
        </button>

        <h3>Parameter passing</h3>
        <span className="badge badge-primary m-2">{this.state.count} </span>
        <button
          className="btn btn-secondary btn-sm"
          onClick={() => this.onHandleIncrement({ id: 1 })}
        >
          Counter+2
        </button>
      </React.Fragment>
    );
  }

  getButtonColor() {
    let classes = "badge m-2 badge-";
    classes += this.state.count === 0 ? "warning" : "primary";
    return classes;
  }

  renderTagsArr() {
    return (
      <ul>
        {this.state.tags.map(tag => (
          <li key={tag}>{tag}</li>
        ))}
      </ul>
    );
  }

  formatCount() {
    return this.state.count === 0 ? "Zero" : this.state.count;
  }

  formatCountJSXExpressions() {
    const { count } = this.state;
    return count === 5 ? <h1>Hell Sense {count}</h1> : count;
  }

  handleIncrement = () => {
    console.log("Hi in func increment");
    // Updating the state
    this.setState({ count: this.state.count + 1 });
  };

  onHandleIncrement = product => {
    console.log(product);
    // Updating the state
    this.setState({ count: this.state.count + 2 });
  };
}

export default Counter;
