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
        title: "Save your Eyes in Digital Life!",
        date: "28/10/2019",
        summary: (
          <p>
            21st century we have been surrounded by screens everywhere &
            excessive dependency on digital lifestyle could lead to weak eye
            sight or eye strain. This article would help you to reduce some
            symptoms related to headache & eye strains.
          </p>
        ),
        body: (
          <p>
            <p>
              Use apps who support Dark Mode extensively if you’re using your
              phone or laptop at night before bed in poor light conditions.
              AMOLED Screens are more beneficial for Dark Mode apps as they
              would turn only the pixels which needs to be lighten up & others
              would be off.
            </p>
            <p>
              <a href="https://medium.com/@kautilyasave/save-your-eyes-in-digital-life-d1269f50c06e">
                Save your Eyes in Digital Life!
              </a>
            </p>
          </p>
        )
      },
      {
        id: 2,
        title: "Apple Watch — Apple iOS Developer’s Perspective.",
        date: "28/11/2019",
        summary:
          "A powerful device at your wrist available 24 x 7 at your disposal.",
        body: (
          <div>
            <p>
              Being a user of Apple Watch S4 for the past month here is my
              conclusive review of the newest series 4 by Apple from iOS
              developer’s perspective. First of all, I would like to start with
              the buyer’s perspective of whether 44k INR / US$ 429 is worth it
              for you? Straight answer: I would say no, yet I went ahead and
              pull the trigger on it. So opting in for No cost EMI x 9 months
              gave me a perspective of investing in my health not directly
              paying just once and getting over it.
            </p>
            <p>
              <a href="https://medium.com/@kautilyasave/a-powerful-device-at-your-wrist-apple-ios-developers-perspective-a9237c51528a">
                Apple Watch S4
              </a>
            </p>
          </div>
        )
      },
      {
        id: 3,
        title: "Top Ten Apple Watch Apps.",
        date: "28/12/2019",
        summary:
          "When Apple released its new product as smartwatch developers & users began to wonder about its use case scenarios in daily life. Over the past few years, Apple has truly worked towards a common goal of making Apple Watch a great accessory or even a necessity. ",
        body: (
          <article>
            <p>
              Watch OS 5 also opens up new possibilities & various API for audio
              streaming apps which overall has also driven more apps released
              specifically for the Watch. A powerful device at your wrist
              available 24 x 7 at your disposal could benefit powerful apps to
              accelerate your lifestyle.
            </p>
            <p>
              <a href="https://medium.com/@kautilyasave/top-ten-apple-watch-apps-4ac3af1eab1f">
                Top Ten Watch OS Apps
              </a>
            </p>
          </article>
        )
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
