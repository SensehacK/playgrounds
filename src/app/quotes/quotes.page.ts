import { Component, OnInit } from '@angular/core';
import { Quote } from 'src/data/quote.interface';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-quotes',
  templateUrl: './quotes.page.html',
  styleUrls: ['./quotes.page.scss'],
})
export class QuotesPage implements OnInit {
  quotePageObj: { category: string, quotes: Quote[], icon: string };
  quoteObjCategory: string;
  quoteObjArr: Quote[];
  quoteObjIcon: string;

  constructor(private router: Router, private routerP: ActivatedRoute) { }

  ngOnInit() {
    console.log("Hello");
    // console.log(this.navParams.data);
    this.routerP.queryParams.subscribe(params => {
      console.log(params.category);
      console.log(params.quotesText);
      console.log('Printing early object');
      console.log(typeof (params.quotesObj));
      console.log('Printing whole object');
      console.log(params.quotesObj.quotes);
      console.log(typeof (params.quotesArr));

      console.log('Printing early quoteLObj2 object');
      console.log(typeof (params.quoteLObj2));

      for (const item in params.quotesObj['quotes']) {
        console.log('in forin loop');
        if (item.hasOwnProperty('person')) {
          const element = item['person'];
          console.log(element);

        }
      }

      // for (const key in object) {
      //   if (object.hasOwnProperty(key)) {
      //     const element = object[key];

      //   }
      // }
      for (const item in params.quotesArr) {
        console.log('Hello WARWTAW');
        console.log(params.quotesArr);
        console.log(item);
        // console.log(item[person]);
        console.log('Hello Sensehack');
      }
      //   * ngfor(items in params.quotesArr) {

      // };
      // this.quoteObjCategory = params[0].category;
    });

  }

}
