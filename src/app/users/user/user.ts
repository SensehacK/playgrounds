import { Component, OnInit } from '@angular/core';
import { UsersPage } from '../users.page';
import { Router } from '@angular/router'
// import { UsersPage } from './user';
// import { NavParams } from '@ionic/angular';

@Component({
    selector: 'page-user',
    templateUrl: 'user.html'
})
export class UserPage implements OnInit {
    name: string;

    // This fucking works, using NavParams has some issues
    // constructor() {
    //     console.log('In UserPage');
    // }

    // constructor(private navParams: NavParams) {
    //     console.log('In UserPage');
    // }

    // constructor(userPage: UsersPage) {
    //     console.log('In UserPage');
    //     this.name = userPage.usersPageName;
    // }

    constructor(private router: Router) {
        // console.log('In UserPage');
        // this.name = userPage.getUserPageName();
    }

    ngOnInit() {
        console.log('In ngOnInit');
        this.name = 'Kautilya';
        console.log(this.router.url);
        // this.name = this.navParams.get('userName');

        // Trying to access variable from Users Page ts file

        // splitting the url values
        // let nameURL = this.router.url;
        // let stringArr = nameURL.split("/");
        // // console.log(nameURL.replace())
        // console.log(stringArr[2]);

        this.name = (this.router.url).split('/')[2];

    }
}
