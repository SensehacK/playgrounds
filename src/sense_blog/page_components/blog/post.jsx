import React, { Component } from "react";

class Post extends Component {
  state = {};

  render() {
    console.log("In Post child component");
    console.log(this.props.postObj);
    // debugger;
    return (
      <div className="postComponent">
        <div className="title">
          <span>Title: {this.props.postObj.title}</span>
        </div>
        <div className="date">
          <span>Date: {this.props.postObj.date}</span>
        </div>
        <div className="summary">
          <span>Summary: {this.props.postObj.summary}</span>
        </div>
        <div className="body">
          <span>Body: {this.props.postObj.body}</span>
        </div>

        <span>Thanks!</span>
        <hr />
      </div>
    );
  }
}

export default Post;
