import { Component, OnInit } from '@angular/core';
import { Quote } from 'src/data/quote.interface';
import { Router, ActivatedRoute } from '@angular/router';
import { DataService } from '../services/data.services';

@Component({
  selector: 'app-quotes',
  templateUrl: './quotes.page.html',
  styleUrls: ['./quotes.page.scss'],
})
export class QuotesPage implements OnInit {
  quotePageData: { category: string, quotes: Quote[], icon: string };
  quoteObjCategory: string;
  quoteObjArr: Quote[];
  quoteObjIcon: string;

  constructor(private router: Router, private routerP: ActivatedRoute, private dataService: DataService) { }

  ngOnInit() {

    console.log('Printing from data service');
    console.log(this.dataService.getQuotePageData());
    this.quotePageData = this.dataService.getQuotePageData();

    console.log('Hello Sensehack printing this.quotePageData');
    console.log(typeof (this.quotePageData));
    console.log(this.quotePageData.category);
    this.quotePageData.quotes.forEach(element => {
      console.log(element.person);

    });



    //calling function of getting data parameters.
    // this.gettingDataParameters();






  }

  gettingDataParameters() {
    // const ar = this.quotePageData();
    console.log('Hello');
    // console.log(this.navParams.data);
    this.routerP.queryParams.subscribe(params => {
      console.log('$%#$^#^^#');
      console.log(params.category);
      console.log(this.quotePageData.category);
      this.quotePageData.category = params.category;
      console.log(this.quotePageData.category);

      console.log('Data of Quotes Category', this.quotePageData.category);

      // Printing console logs for trial & error
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
