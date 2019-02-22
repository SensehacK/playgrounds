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
    // this.navCtrl.navigateForward('/users');
    // this.router.navigate(['users']); // Send path/ object in array
    // this.router.navigateByUrl('/users'); // Send path/ object in URL string

    // checking with local authentication
    this.router.navigate(['users']).catch((error) => console.log('Access is Denied' + error));
  }

  onGoToShop() {
    this.router.navigate(['shop']);
  }

  onGoToBuy() {
    this.router.navigate(['buy']);
    // this.router.navigateByUrl('/buyout');
  }
}
