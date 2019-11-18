import React, { Component } from 'react';
import NavBar from './component/navbar';
import Counters from './component/counters'

class App extends Component {

    state = {
        counters: [
            { id: 1, value: 0 },
            { id: 2, value: 3 },
            { id: 3, value: 2 },
            { id: 4, value: 3 }
        ]
    };

    resetCounters = () => {
        const counters = this.state.counters.map(c => {
            c.value = 0;
            return c;
        });
        this.setState({ counters });
    };

    handleIncrement = counterID => {
        // console.log(counterID);
        const counters = [...this.state.counters];
        const index = counters.indexOf(counterID);
        counters[index] = { ...counterID };
        counters[index].value++;
        this.setState({ counters });
        // but the setState is async so the change doesn't appear right away
        // console.log("Printing Main counters", this.state.counters);
    };

    handleDelete = counterID => {
        console.log("Delete func called", counterID);
        const counters = this.state.counters.filter(c => c.id !== counterID);
        // this.state.counters = counters; We can set state like this, React won't notice the change management like angular
        this.setState({ counters: counters }); // Simplify setState ({counters}) As both are same, destructive construction object something
    };


    render() {
        return (
            <React.Fragment>
                <NavBar
                    totalCounters={this.state.counters.filter(c => c.value > 0).length}
                />
                <main className="container">
                    <Counters
                        counters={this.state.counters}
                        onReset={this.resetCounters}
                        onIncrement={this.handleIncrement}
                        onDelete={this.handleDelete}
                    />
                </main>
            </React.Fragment>
        );
    }
}

export default App;