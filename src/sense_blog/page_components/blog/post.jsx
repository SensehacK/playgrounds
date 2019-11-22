import React, { Component } from "react";

class Post extends Component {
  state = {};
  render() {
    console.log("In Post component");

    console.log(this.props.postObj);
    // debugger;
    return (
      <React.Fragment>
        <h3>Counter #{this.props.id}</h3>
        <div className="title">
          <p>Title: {this.props.postObj.title}</p>
        </div>
        <div className="date">
          <p>Date: {this.props.postObj.date}</p>
        </div>
        <div className="summary">
          <p>Summary: {this.props.postObj.summary}</p>
        </div>
        <div className="body">
          <p>Body: {this.props.postObj.body}</p>
        </div>
      </React.Fragment>
    );
  }
}

export default Post;
