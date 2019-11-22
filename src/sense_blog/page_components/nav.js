import React, { Component } from 'react';

class Nav extends Component {
    state = {}
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