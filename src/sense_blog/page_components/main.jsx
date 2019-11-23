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
        date: "28/10/2019",
        summary: "HEDFAFW",
        body: (
          <div>
            <p>Dark Mode</p>

            <p>
              Use apps who support Dark Mode extensively if you&rsquo;re using
              your phone or laptop at night before bed in poor light conditions.
            </p>

            <p>
              AMOLED Screens are more beneficial for Dark Mode apps as they
              would turn only the pixels which needs to be lighten up &amp;
              others would be off. &quot;Dark Mode\n&quot; + \n&quot; + Use apps
              who support Dark Mode extensively if you&rsquo;re using your phone
              or laptop at night before bed in poor light conditions.\n&quot; +
              \n&quot; + AMOLED Screens are more beneficial for Dark Mode apps
              as they would turn only the pixels which needs to be lighten up
              &amp; others would be off.\n&quot; + &quot;
            </p>
          </div>
        )
      },
      {
        id: 2,
        title: "Dummy_Title 2",
        date: "28/11/2019",
        summary: "HEDFAFW",
        body:
          "Lorem ipsum dolor sit, amet consectetur adipisicing elit. A doloribus architecto voluptatibus ab iusto magni consequuntur \n" +
          "fuga quas deserunt aspernatur unde, veritatis non, sapiente officiis officia recusandae hic commodi voluptatum, excepturi odio quod! \n" +
          "Obcaecati saepe velit cumque sapiente in, nemo tenetur, aspernatur porro beatae dolorem sunt maiores error. Placeat blanditiis excepturi \n" +
          "alias ex maxime earum eum dolore tempore. Optio qui, sapiente voluptatem laborum quis corporis voluptate error eligendi nihil \n" +
          "autem officia recusandae odit tenetur totam amet, adipisci, iusto atque quia tempore modi. Sunt, excepturi praesentium vero enim ex\n" +
          "earum similique quibusdam, consectetur pariatur ut aut nihil? Molestiae inventore eum qui?"
      },
      {
        id: 3,
        title: "Dummy_Title 3",
        date: "28/12/2019",
        summary: "HEDFAFW",
        body:
          "Lorem ipsum dolor sit, amet consectetur adipisicing elit. A doloribus architecto voluptatibus ab iusto magni consequuntur \n" +
          "fuga quas deserunt aspernatur unde, veritatis non, sapiente officiis officia recusandae hic commodi voluptatum, excepturi odio quod! \n" +
          "Obcaecati saepe velit cumque sapiente in, nemo tenetur, aspernatur porro beatae dolorem sunt maiores error. Placeat blanditiis excepturi \n" +
          "alias ex maxime earum eum dolore tempore. Optio qui, sapiente voluptatem laborum quis corporis voluptate error eligendi nihil \n" +
          "autem officia recusandae odit tenetur totam amet, adipisci, iusto atque quia tempore modi. Sunt, excepturi praesentium vero enim ex\n" +
          "earum similique quibusdam, consectetur pariatur ut aut nihil? Molestiae inventore eum qui?"
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
