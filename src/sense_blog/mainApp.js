import React, { Component } from 'react';
import Main from './page_components/main'
import Header from './page_components/header';
import Nav from './page_components/nav';
import Footer from './page_components/footer';


class MainApp extends Component {
    state = {}
    render() {
        return (
            <div>
                <h1>Hello Sensehack!</h1>
                <Header />
                <Main />
                <Nav />
                <Footer />
            </div>

        );
    }
}

export default MainApp;