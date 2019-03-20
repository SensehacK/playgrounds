import { Component, OnInit } from '@angular/core';
import { Recipe } from './recipe.model';
import { RecipesService } from './recipes.service';

@Component({
  selector: 'app-recipes',
  templateUrl: './recipes.page.html',
  styleUrls: ['./recipes.page.scss']
})
export class RecipesPage implements OnInit {
  localRecipe: Recipe[];

  constructor(private recipeService: RecipesService) {}

  ngOnInit() {
    this.localRecipe = this.recipeService.getAllRecipes();
  }

  ionViewWillEnter() {
    console.log('in Ion View Will Enter');

    this.localRecipe = this.recipeService.getAllRecipes();
  }
}
