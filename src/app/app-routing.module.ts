import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', loadChildren: './home/home.module#HomePageModule' },
  { path: 'library', loadChildren: './library/library.module#LibraryPageModule' },
  { path: 'quotes', loadChildren: './quotes/quotes.module#QuotesPageModule' },
  { path: 'quote', loadChildren: './quote/quote.module#QuotePageModule' },
  { path: 'favorites', loadChildren: './favorites/favorites.module#FavoritesPageModule' },
  { path: 'settings', loadChildren: './settings/settings.module#SettingsPageModule' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
