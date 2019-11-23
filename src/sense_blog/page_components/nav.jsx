import React, { Component } from "react";
import { log } from "util";

class Nav extends Component {
  state = {
    statePosts: [],
    isLoaded: false
  };

  isLoaded = false;
  data = [];

  constructor() {
    super();
    var url =
      "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + apiKey;

    console.log(url);

    var req = new Request(url);

    console.log(req);

    var data2 = fetch(req).then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Server response wasn't OK");
      }

      // console.log("fetch response back");
      // console.log(response.json());
      // debugger;
      // console.log(response.articles);

      // this.isLoaded = true;

      // console.log(response["articles"]);

      // console.log(typeof response);
      // console.log(response.json()["articles"]);
      // this.data = response.json();
    });

    console.log("Hi checking response data");

    console.log(data2);
  }
  componentDidMount() {
    var url =
      "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + apiKey;

    // Without using await keyword, async programming
    const newsapi = fetch(url)
      .then(data => data.json())
      .then(articles => articles["articles"]);

    // Unwrapping the data of a async promise
    newsapi.then(jsonD => {
      this.setState({
        statePosts: jsonD,
        isLoaded: true
      });
    });

    // console.log(newsapi["articles"]);

    // if (this.isLoaded) {
    //   this.setState({
    //     statePosts: this.data
    //   });
    // }
  }

  // componentWillMount() {}

  render() {
    return (
      <aside>
        <ul>
          <li>
            <a href="https://github.com/" title="Github" target="_blank">
              Github
            </a>
          </li>
          <li>
            <a href="https://www.linkedin.com/" target="_blank">
              LinkedIn
            </a>
          </li>

          <li>
            <a href="https://www.instagram.com/" target="_blank">
              Instagram
            </a>
          </li>

          <li>
            <a href="https://www.reddit.com/" title="Xbox" target="_blank">
              Reddit
            </a>
          </li>

          <li>
            <a href="https://trakt.tv/" title="Trakt TV" target="_blank">
              TraktTV
            </a>
          </li>
        </ul>
      </aside>
    );
  }
}

export default Nav;
