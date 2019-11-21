import React, { Component } from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCoffee } from '@fortawesome/free-solid-svg-icons';


class Footer extends Component {
    state = {}
    render() {
        return (
            <div>
                <p> Footer Class!</p>
                <FontAwesomeIcon icon={faCoffee} />
            </div>
        );
    }
}

export default Footer;