import { Component } from '@angular/core';
import { FavoritesPage } from '../favorites/favorites.page';
import { LibraryPage } from '../library/library.page';
import { QuotePage } from '../quote/quote.page';

@Component({
    selector: 'page-tabs',
    templateUrl: 'tabs.page.html',
})

export class TabsPage {
    favoritesPage = FavoritesPage;
    libraryPage = LibraryPage;
    quotePage = QuotePage;
    constructor() {
        console.log('Hello SEnsehacK');
    }

}
