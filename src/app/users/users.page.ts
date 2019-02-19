import { Component, OnInit } from '@angular/core';
import { NavController } from '@ionic/angular';
// import { UserPage } from './user/user';
import { Router } from '@angular/router';
@Component({
  selector: 'app-users',
  templateUrl: './users.page.html',
  styleUrls: ['./users.page.scss'],
})
export class UsersPage {
  usersPageName: string;
  constructor(private navCtrl: NavController, private router: Router) { }

  onLoadUser(name: string) {
    console.log('Hello On Load User', name);
    // Setting name send by HTML & saving it in variable usersPageName
    this.usersPageName = name;

    // Different Navigation Angular Routing Techniques Trial & Error.
    // this.navCtrl.navigateForward('UserPage', { queryParams: { 'userName': name } });

    // this.navCtrl.navigateForward(UserPage, { queryParams: { 'userName': name } });
    // this.router.navigate([UserPage], name);
    // this.router.navigateByUrl('./user/user#UserPage');
    this.router.navigate([`user/${name}`]);

    // this.router.navigate(UserPage, { userName: name });

  }

  public getUserPageName() {
    return this.usersPageName;
  }


}
