import { Injectable } from '@angular/core';
import { Quote } from 'src/data/quote.interface';

@Injectable({
    providedIn: 'root'
})

export class DataService {
    private message: string;
    private quotePageData: { category: string, quotes: Quote[], icon: string };

    constructor() {
        this.message = 'Hello Sensehack';

    }

    getMessage() {
        return this.message;
    }

    getQuotePageData() {
        return this.quotePageData;
    }

    setQuotePageData(dataObj: any) {
        this.quotePageData = dataObj;

    }
}
