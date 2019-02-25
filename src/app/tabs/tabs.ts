import { Component } from '@angular/core';
import { FavoritesPage } from '../favorites/favorites.page';
import { LibraryPage } from '../library/library.page';

@Component({
    selector: 'page-tabs',
    templateUrl: 'tabs.page.html',
})

export class TabsPage {
    favoritesPage = FavoritesPage;
    libraryPage = LibraryPage;
    constructor() {
        console.log('Hello SEnsehacK');
    }

}
