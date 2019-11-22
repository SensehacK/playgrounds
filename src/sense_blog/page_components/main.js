import React, { Component } from 'react';

import Post from './blog/post';

class Main extends Component {
    state = {
        blog: [
            {
                id: 1,
                title: 'Dummy_Title',
                date: '28/11/2019',
                summary: 'HEDFAFW',
                body: 'HEDFAFW',
            },
            {
                id: 2,
                title: 'Dummy_Title',
                date: '28/11/2019',
                summary: 'HEDFAFW',
                body: 'HEDFAFW',
            },
            {
                id: 3,
                title: 'Dummy_Title',
                date: '28/11/2019',
                summary: 'HEDFAFW',
                body: 'HEDFAFW',
            }
        ]
    }

    render() {
        return (
            <div>
                <main>
                    {this.state.blog.map(post => (
                        <div>
                            {/* <h1>{post}</h1> */}
                            <Post
                                key={post.id}
                                id={post.id}
                                postObj={post}
                            />
                        </div>

                    ))}
                    <p>
                        I'm an iOS based app developer, web designer and technophile.
					<br />
                        Fusing technology with lifestyle to foster something phenomenal as
                        SensehacK.
					<br />
                        <span>Become my Nakama !</span>
                    </p>
                </main>
                <p>Main Class!</p>
            </div >
        );
    }
}

export default Main;