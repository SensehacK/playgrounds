import React, { Component } from "react";
import Main from "./page_components/main";
import Header from "./page_components/header";
import Nav from "./page_components/nav";
import Social from "./page_components/social";
import Footer from "./page_components/footer";

class MainApp extends Component {
  state = {};
  render() {
    const myStyle = {
      color: "#63d913"
    };
    return (
      <div>
        <Header />
        <section>
          <Main />
          <Nav />
        </section>
        <Social />
        <h1 style={myStyle}>Hello Sensehack!</h1>
        <Footer />
      </div>
    );
  }
}

export default MainApp;
