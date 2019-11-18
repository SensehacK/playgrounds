import React, { Component } from 'react';
import NavBar from './component/navbar';
import Counters from './component/counters'

class App extends Component {
    state = {}
    render() {
        return (
            <React.Fragment>
                <NavBar />
                <main className="container">
                    <Counters />
                </main>
            </React.Fragment>
        );
    }
}

export default App;