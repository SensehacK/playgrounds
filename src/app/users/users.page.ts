import { Component, OnInit } from '@angular/core';
import { NavController } from '@ionic/angular';
import { UserPage } from './user/user';
import { Router } from '@angular/router';
@Component({
  selector: 'app-users',
  templateUrl: './users.page.html',
  styleUrls: ['./users.page.scss'],
})
export class UsersPage {

  constructor(private navCtrl: NavController, private router: Router) { }

  onLoadUser(name: string) {
    // this.navCtrl.navigateForward('UserPage', { queryParams: { 'userName': name } });
    console.log('Hello On Load User');
    this.navCtrl.navigateForward('UserPage', { queryParams: { 'userName': name } });
    // this.router.navigate([UserPage], name);
    // this.navCtrl.naviga
    // this.router.navigate(UserPage, { userName: name });

  }


}
