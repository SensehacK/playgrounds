import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { TabsPage } from './tabs';
import { FavoritesPage } from '../favorites/favorites.page';
import { LibraryPage } from '../library/library.page';
import { QuotePage } from '../quote/quote.page';
import { QuotesPage } from '../quotes/quotes.page';
import { SettingsPage } from '../settings/settings.page';
import { QuotesPageModule } from '../quotes/quotes.module';
import { SettingsPageModule } from '../settings/settings.module';

const routes: Routes = [
    {
        path: 'tabs',
        component: TabsPage,
        children: [
            {
                path: 'favorites',
                children: [
                    {
                        path: '',
                        loadChildren: './favorites/favorites.module#FavoritesPageModule'
                    }
                ]
            },
            {
                path: 'library',
                children: [
                    {
                        path: '',
                        loadChildren: './library/library.module#LibraryPageModule'
                    }
                ]
            },
            {
                path: 'quotes',
                children: [
                    {
                        path: '',
                        loadChildren: './quotes/quotes.module#QuotesPageModule'
                    }
                ]
            },
            {
                path: 'quote',
                children: [
                    {
                        path: '',
                        loadChildren: './quote/quote.module#QuotePageModule'
                    }
                ]
            }
        ]

    },
    {
        path: '',
        redirectTo: '/tabs/tabs',
        pathMatch: 'full'
    }
];

@NgModule({
    imports: [
        CommonModule,
        FormsModule,
        IonicModule,
        RouterModule.forChild(routes)
        // RouterModule.forChild([
        //     {
        //         path: '',
        //         component: TabsPage
        //     }
        // ])
    ],
    exports: [RouterModule],
    declarations: [TabsPage]
})
export class TabsPageModule { }
