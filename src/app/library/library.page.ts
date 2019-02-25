import { Component, OnInit } from '@angular/core';
import { Quote } from 'src/data/quote.interface';
import quotes from 'src/data/quotes';
import { QuotesPage } from '../quotes/quotes.page';
import { Router } from '@angular/router';

@Component({
  selector: 'app-library',
  templateUrl: './library.page.html',
  styleUrls: ['./library.page.scss'],
})
export class LibraryPage implements OnInit {

  constructor(private router: Router) { }

  quoteCollection: { category: string, quotes: Quote[], icon: string }[];
  quoteObj: { category: string, quotes: Quote[], icon: string };
  quotesPage: QuotesPage;

  ngOnInit() {
    this.quoteCollection = quotes;

  }

  goToQuotesPage(quoteL: any) {
    console.log(quoteL);
    const navigationExt = {
      queryParams: { 'category': quoteL.category, 'quotesText': quoteL.quotes[0].text, 'quotesArr': quoteL.quotes, 'quotesObj': quoteL, 'quoteLObj2': this.quoteObj }
    };
    this.quoteObj = quoteL;
    console.log('printing selected index object');
    console.log(quoteL);
    console.log(quoteL.quotes);
    this.router.navigate(['quotes'], navigationExt);


    // this.router.navigate(['quotes'], quoteL);
  }



}
