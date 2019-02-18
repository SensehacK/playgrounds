import { Component } from '@angular/core';
import { NavController } from '@ionic/angular';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  constructor(private navCtrl: NavController, private router: Router) {

  }

  onGoToUsers() {
    // this.navC trl.navigateForward('/users');
    // this.router.navigate(['/users']);
    this.router.navigateByUrl('/users');
  }
}
