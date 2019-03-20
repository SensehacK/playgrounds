import { Component, OnInit } from '@angular/core';
import { Recipe } from './recipe.model';
import { RecipesService } from './recipes.service';
import { RecipeMaster } from './recipeMaster.model';

@Component({
  selector: 'app-recipes',
  templateUrl: './recipes.page.html',
  styleUrls: ['./recipes.page.scss']
})
export class RecipesPage implements OnInit {
  localRecipe: Recipe[];
  recipeMaster: RecipeMaster[];

  constructor(private recipeService: RecipesService) {}

  ngOnInit() {
    this.localRecipe = this.recipeService.getAllRecipes();
    this.recipeMaster = this.recipeService.getAllMasterRecipes();
    this.recipeMaster.forEach(recipe => {
      console.log('printing images URL');
      console.log(recipe.imageURL);
    });
  }

  ionViewWillEnter() {
    console.log('in Ion View Will Enter');

    this.localRecipe = this.recipeService.getAllRecipes();
    this.recipeMaster = this.recipeService.getAllMasterRecipes();
  }
}
