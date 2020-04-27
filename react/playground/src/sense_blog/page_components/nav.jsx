import React, { Component } from "react";
// import { config } from "../../config";

class Nav extends Component {
  state = {
    statePosts: [],
    isLoaded: false
  };

  constructor() {
    super();
    console.log("In Nav, trying to access keys from config file");

    // console.log(config.SECRET_KEY);
  }

  componentDidMount() {
    var apiKey = "YOUR_GOOGLE_WEB_API_KEY";
    var url =
      "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + apiKey;

    setInterval(async () => {
      // Without using await keyword, async programming
      const newsApi = fetch(url)
        .then(data => data.json())
        .then(articles => articles["articles"]);

      console.log("Hi in NewsAPI");

      // Unwrapping the data of a async promise
      newsApi.then(jsonD => {
        console.log(jsonD);
        this.setState({
          statePosts: jsonD,
          isLoaded: true
        });
      });
    }, 5000);
  }

  render() {
    console.log("Hi in Nav news Api");

    const { statePosts, isLoaded } = this.state;
    if (isLoaded) {
      return (
        <nav>
          <div>
            <ul>
              <li>
                <a href="/">Home</a>
              </li>
              {statePosts &&
                statePosts.map((post, key) => <li key={key}>{post.title}</li>)}
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
