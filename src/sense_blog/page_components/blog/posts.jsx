import React, { Component } from "react";
import Post from "./post";
import ArticlesData from "../assets/articles.json";

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
        {/* Two Methods of accessing the same data */}
        <div>
          {/* Local Obj from React State */}
          <h2>Hello Kautilya</h2>
          {statePosts.map(post => (
            <Post key={post.id} postObj={post} />
          ))}
        </div>

        <div>
          {/* Local JSON import and direct map */}
          <h2>Hello Sensehack</h2>
          {ArticlesData.map((post, key) => (
            <Post key={key} postObj={post} />
          ))}
        </div>
      </div>
    );
  }
}

export default Posts;
