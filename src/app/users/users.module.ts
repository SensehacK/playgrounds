import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { UsersPage } from './users.page';
import { AdminComponent } from './admin/admin.component';

const routes: Routes = [
  {
    path: '',
    component: UsersPage
  },
  {
    path: 'id',
    component: AdminComponent
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [UsersPage, AdminComponent]
})
export class UsersPageModule { }
