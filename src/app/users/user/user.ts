import { Component, OnInit } from '@angular/core';
import { UsersPage } from '../users.page';
import { Router, ActivatedRoute } from '@angular/router';
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

    constructor(private router: Router, private activeRoute: ActivatedRoute) {
        console.log('In UserPage');
        // this.name = userPage.getUserPageName();
    }

    ngOnInit() {
        // calling function to set Name
        this.setName();

    }

    setName() {
        // Inefficient method of accessing URL path
        console.log('In ngOnInit');
        this.name = 'Kautilya';
        // console.log(this.router);
        this.name = (this.router.url).split('/')[2];

        // second method of accessing router params object values / Right way
        console.log(this.activeRoute);
        console.log(this.activeRoute.params);
        const valueRoute = this.activeRoute.params;
        console.log(valueRoute['value'].name);
    }
    onGoBack() {
        console.log('in function Go back');
        this.router.navigate(['users']);
        // this

    }
}
