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
        console.log('Helo SEnsehacK');
        // <ion-tab [root]="favoritesPage" tabTitle="Favorites" tabIcon="star"> </ion-tab>
        // <ion-tab [root]="libraryPage" tabTitle="Library" tabIcon="book"> </ion-tab>template: '

        /* `
     <ion-tabs>
     <p> Hello </p>
     <ion-tab tab="favoritesPage">
     <ion-router-outlet name="favoritesPage"></ion-router-outlet>
     </ion-tab>
     <ion-tab tab="libraryPage">
     <ion-router-outlet name="libraryPage"></ion-router-outlet>
     </ion-tab>
     </ion-tabs>
     `
 */

    }

}
