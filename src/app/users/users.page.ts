import { Component, OnInit } from '@angular/core';
import { NavController } from '@ionic/angular';
// import { UserPage } from './user/user';
import { Router, ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-users',
  templateUrl: './users.page.html',
  styleUrls: ['./users.page.scss'],
})
export class UsersPage {
  usersPageName: string;
  urlPath: string;

  constructor(private navCtrl: NavController, private router: Router, private activeRou: ActivatedRoute) {
    console.log('before ionViewCanEnter');
    this.setUpPage();

  }

  // ngOnInit() {
  //   this.urlPath = this.activeRou.snapshot.paramMap.get('id');
  // }

  ionViewCanEnter(): boolean {
    console.log('ionViewCanEnter');

    // return true;
    return false;

  }

  ionViewWillEnter() {
    console.log('ionViewWillEnter');
  }

  onLoadUser(name: string) {
    console.log('Hello On Load User', name);
    // Setting name send by HTML & saving it in variable usersPageName
    this.usersPageName = name;

    // Different Navigation Angular Routing Techniques Trial & Error.
    // this.navCtrl.navigateForward('UserPage', { queryParams: { 'userName': name } });

    // this.navCtrl.navigateForward(UserPage, { queryParams: { 'userName': name } });
    // this.router.navigate([UserPage], name);
    // this.router.navigateByUrl('./user/user#UserPage');
    // Send parameter String directly in URL with angular navigation.
    this.router.navigate([`user/${name}`]);

    // this.router.navigate(UserPage, { userName: name });

  }

  public getUserPageName() {
    return this.usersPageName;
  }

  setUpPage() {
    this.urlPath = this.activeRou.snapshot.paramMap.get('id');
  }


}
