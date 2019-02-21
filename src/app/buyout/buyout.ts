import { Component, Input } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
    selector: 'page-buyout',
    templateUrl: 'buyout.html'
})

export class BuyoutPage {
    // @Input() parentData: object;
    parentData1: string;
    @Input() productData: any;
    productData2: { name: string, quantity: number };
    productName: string;
    productQty: number;

    constructor(private router: Router, private activeRoute: ActivatedRoute) {
        // console.log(this.parentData['name']);
        // this.productData = { name: "milk" }
        console.log('in buyout Page');
        this.parentData1 = 'Kautilya';
        console.log(this.productData);
        console.log(this.parentData1);
        // this.parentData1 = this.parentData['name'];

        // Calling function for parsing data which is retrieved.
        this.retrieveData();
    }

    retrieveData() {
        console.log('In ngOnInit');
        this.parentData1 = 'Kautilya';
        console.log(this.activeRoute.params);
        console.log('Selected values are:');
        const valueRoute = (this.activeRoute.params['value'].id);
        // Save split values in variables.
        this.productName = valueRoute.split(' ')[0];
        this.productQty = Number(valueRoute.split(' ')[1]);

        console.log(typeof (this.productQty));

        // Printing data retrieved via URL path
        console.log('local variables');
        console.log('Name:', this.productName);
        console.log('Quantity:', this.productQty);

        // Try to save it in object | first method works & without { } doesn't work but for retrieving data it works just independently.
        this.productData2 = { name: this.productName, quantity: this.productQty };


        /* second method. If I save it with this method it gives this error : Uncaught (in promise): 
        // TypeError: Cannot set property 'name' of undefined
        this.productData2['name'] = this.productName;
        this.productData2['name'] = "Kautilya";
        this.productData2['quantity'] = this.productQty;
        */



        // Printing data stored from local obj
        console.log('local obj');
        console.log('Name:', this.productData2.name);
        console.log('Quantity:', this.productData2.quantity);
        // console.log((this.activeRoute.params['value'].id).split(' ')[1]);

    }

}
