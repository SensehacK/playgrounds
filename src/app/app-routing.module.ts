import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', loadChildren: './home/home.module#HomePageModule' },
  { path: 'users', loadChildren: './users/users.module#UsersPageModule' },
  { path: 'user/:name', loadChildren: './users/user/user.module#UserPageModule' },
  { path: 'users/:id', loadChildren: './users/users.module#UsersPageModule' },
  { path: 'shop', loadChildren: './shop/shop.module#ShopPageModule' },
  { path: 'buy', loadChildren: './buyout/buyout.module#BuyoutPageModule' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
