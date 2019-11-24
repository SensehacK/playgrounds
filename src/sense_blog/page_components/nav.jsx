import React, { Component } from "react";
import { config } from "../../config";

class Nav extends Component {
  state = {
    statePosts: [],
    isLoaded: false
  };

  constructor() {
    super();
    console.log("In Nav, trying to access keys from config file");

    console.log(config.SECRET_KEY);
  }

  componentDidMount() {
    var url =
      "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + apiKey;

    // Without using await keyword, async programming
    const newsApi = fetch(url)
      .then(data => data.json())
      .then(articles => articles["articles"]);

    // Unwrapping the data of a async promise
    newsApi.then(jsonD => {
      this.setState({
        statePosts: jsonD,
        isLoaded: true
      });
    });
  }

  render() {
    const { statePosts, isLoaded } = this.state;
    if (isLoaded) {
      return (
        <nav>
          <div>
            <ul>
              {statePosts.map((post, key) => (
                <li key={key}>{post.title}</li>
              ))}
            </ul>
          </div>
        </nav>
      );
    } else {
      return (
        <aside>
          <h2>Network Request Loading</h2>
        </aside>
      );
    }
  }
}

export default Nav;
