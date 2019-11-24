import React, { Component } from "react";
// import { Link } from "react-router";
import { BrowserRouter, Route, Link } from "react-router-dom";

class Post extends Component {
  state = {};

  render() {
    console.log("In Post child component");
    var { postObj } = this.props;
    console.log(postObj);
    console.log("/post" + postObj.id);

    return (
      // <Link to {} > </Link>
      <div className="postComponent">
        <Link to={`/post${postObj.id}`}>
          <div className="title">
            <span>Title: {postObj.title}</span>
          </div>
        </Link>
        <div className="date">
          <span>Date: {postObj.date}</span>
        </div>
        <div className="summary">
          <span>Summary: {postObj.summary}</span>
        </div>
        <div className="body">
          <span>Body: {postObj.body}</span>
        </div>
        <div className="link">
          <span>
            <a href={postObj.ogUrl}>{postObj.ogUrl}</a>
          </span>
        </div>
        <hr />
      </div>
    );
  }
}

export default Post;
