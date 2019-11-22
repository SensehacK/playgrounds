import React, { Component } from "react";
import Post from "./post";

class Posts extends Component {
  state = {
    statePosts: []
  };

  componentWillMount() {
    console.log("Component Will mount");
    // setting temporary array back to state
    const posts = [];
    this.props.postsObj.map(post => posts.push(post));
    this.setState({
      statePosts: posts
    });
  }

  render() {
    console.log("In Posts component");
    var { statePosts } = this.state;
    return (
      <div>
        <h1>Hello Kautilya Posts Parent</h1>
        {statePosts.map(post => (
          <Post key={post.id} postObj={post} />
        ))}
      </div>
    );
  }
}

export default Posts;
