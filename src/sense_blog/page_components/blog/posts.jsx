import React, { Component } from "react";
import Post from "./post";

class Posts extends Component {
  state = {
    statePosts: []
  };

  componentWillMount() {
    // setting temporary array back to state
    const posts = [];
    this.props.postsObj.map(post => posts.push(post));
    this.setState({
      statePosts: posts
    });
  }

  render() {
    var { statePosts } = this.state;
    return (
      <div>
        <h1>Hello Kautilya</h1>
        {statePosts.map(post => (
          <Post key={post.id} postObj={post} />
        ))}
      </div>
    );
  }
}

export default Posts;
