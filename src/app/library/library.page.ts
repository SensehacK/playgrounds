import { Component, OnInit } from '@angular/core';
import { Quote } from 'src/data/quote.interface';
import quotes from 'src/data/quotes';
import { QuotesPage } from '../quotes/quotes.page';
import { Router } from '@angular/router';
import { DataService } from '../services/data.services';

@Component({
  selector: 'app-library',
  templateUrl: './library.page.html',
  styleUrls: ['./library.page.scss']
})
export class LibraryPage implements OnInit {
  constructor(private router: Router, private dataService: DataService) {}

  quoteCollection: { category: string; quotes: Quote[]; icon: string }[];
  quoteObj: { category: string; quotes: Quote[]; icon: string };
  quotesPage: QuotesPage;

  ngOnInit() {
    this.quoteCollection = quotes;
  }

  goToQuotesPage(quoteL: any) {
    // Trying to set object data in data service
    this.dataService.setQuotePageData(quoteL);
    console.log('Printing from data service');
    console.log(this.dataService.getQuotePageData());

    console.log(quoteL);
    const navigationExt = {
      queryParams: {
        category: quoteL.category,
        quotesText: quoteL.quotes[0].text,
        quotesArr: quoteL.quotes,
        quotesObj: quoteL,
        quoteLObj2: this.quoteObj
      }
    };
    this.quoteObj = quoteL;
    console.log('printing selected index object');
    console.log(quoteL);
    console.log(quoteL.quotes);
    this.router.navigate(['quotes'], navigationExt);
    console.log('Hei');

    // this.router.navigate(['quotes'], quoteL);
  }
}
