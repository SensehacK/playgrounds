import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-shop',
  templateUrl: './shop.page.html',
  styleUrls: ['./shop.page.scss'],
})
export class ShopPage {

  constructor(private router: Router) {

  }
  productData: { name: string, quantity: number };
  // shopPObj: ShopPage();
  nameQty: string;

  onBuyout(productData: { name: string, quantity: number }) {


    console.log(productData);
    console.log(typeof (productData));

    this.productData = productData;
    console.log(this.productData);
    let nameQ: string
    this.nameQty = this.productData.name + this.productData.quantity;
    nameQ = this.productData.name + ' ' + this.productData.quantity;
    console.log(nameQ);
    console.log(typeof (nameQ));
    this.router.navigate([`buy/${nameQ}`]);

    // this.router.navigate([`buy/${productData.name, productData.quantity}`]);
  }
}
