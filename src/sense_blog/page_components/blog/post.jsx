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

        <p>Thanks!</p>
        <hr />
      </div>
    );
  }
}

export default Post;
