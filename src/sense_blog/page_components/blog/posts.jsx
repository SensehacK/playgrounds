import React, { Component } from "react";
import Post from "./post";

class Posts extends Component {
  state = {
    statePosts: []
  };

  componentWillMount() {
    // this.setState({
    //   posts: this.props.postsObj
    // });
    console.log("COmponent Will mount");
    const posts = [];
    this.props.postsObj.map(post => posts.push(post));
    // setting temporary array back to state

    this.setState({
      statePosts: posts
    });
  }

  render() {
    console.log("In Posts component");

    console.log(this.props.postsObj);

    var { statePosts } = this.state;
    console.log("In render posts");

    console.log(statePosts);

    var postOb1 = statePosts[0];

    // debugger;
    return (
      <div>
        <h1>Hello Kautilya Posts Parent</h1>
        <div>
          {statePosts.map(
            post => (
              (<Post key={post.id} postObj={post} />),
              console.log("Post Id", post.id),
              console.log("Hi Map function", post)
            )
          )}

          {/* <Post obj={postOb1} /> */}

          {/* {counters.map(counter => (
            <SingularCounter
              key={counter.id}
              onIncrement={onIncrement}
              onDelete={onDelete}
              counter={counter}
              // id={counter.id}
            />
          ))} */}
        </div>

        {/* <div className="title">
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
        </div> */}
      </div>
    );
  }
}

export default Posts;
