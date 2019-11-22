import React, { Component } from "react";
import { Route, Switch } from "react-router";
import { HashRouter } from "react-router-dom";
import Post from "./blog/post";
import Posts from "./blog/posts";

class Main extends Component {
  state = {
    blog: [
      {
        id: 1,
        title: "Dummy_Title 1",
        date: "28/11/2019",
        summary: "HEDFAFW",
        body: "HEDFAFW"
      },
      {
        id: 2,
        title: "Dummy_Title 2",
        date: "28/11/2019",
        summary: "HEDFAFW",
        body: "HEDFAFW"
      },
      {
        id: 3,
        title: "Dummy_Title 3",
        date: "28/11/2019",
        summary: "HEDFAFW",
        body: "HEDFAFW"
      }
    ]
  };

  render() {
    return (
      <main>
        <HashRouter>
          <Switch>
            <Route
              exact
              path="/"
              render={props => <Posts postsObj={this.state.blog} />}
            />
            <Route
              path="/post1"
              render={props => <Post postObj={this.state.blog[0]} />}
            />
            <Route
              path="/post2"
              render={props => <Post postObj={this.state.blog[1]} />}
            />
            <Route
              path="/post3"
              render={props => <Post postObj={this.state.blog[2]} />}
            />
          </Switch>
        </HashRouter>
      </main>
    );
  }
}

export default Main;
