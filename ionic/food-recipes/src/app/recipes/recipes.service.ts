import { Injectable } from '@angular/core';
import { Recipe } from './recipe.model';
import { RecipeMaster } from './recipeMaster.model';
import { utils } from 'protractor';
// import data from 'src/app/recipes/reci';

@Injectable({
  providedIn: 'root'
})
export class RecipesService {
  private recipesArr: Recipe[] = [
    {
      id: 'r1',
      title: 'Tomato Pasta',
      imageURL:
        'https://drop.ndtv.com/albums/COOKS/pasta-vegetarian/pastaveg_640x480.jpg',
      ingredients: ['French Pasta', 'Tomato', 'Salad']
    },
    {
      id: 'r2',
      title: 'Steak',
      imageURL:
        'https://images.pexels.com/photos/46239/salmon-dish-food-meal-46239.jpeg?cs=srgb&dl=close-up-cooking-dinner-46239.jpg&fm=jpg',
      ingredients: ['Meat', 'Tomato', 'Salad']
    },
    {
      id: 'r3',
      title: 'Pasta',
      imageURL:
        'https://drop.ndtv.com/albums/COOKS/pasta-vegetarian/pastaveg_640x480.jpg',
      ingredients: ['French Pasta', 'Tomato', 'Salad']
    },
    {
      id: 'r4',
      title: 'Beef',
      imageURL:
        'https://images.pexels.com/photos/46239/salmon-dish-food-meal-46239.jpeg?cs=srgb&dl=close-up-cooking-dinner-46239.jpg&fm=jpg',
      ingredients: ['Meat', 'Onion', 'Salad']
    }
  ];

  // let routesObject:  = require('./src/app/recipes/recipeMaster.json');

  private recipeMaster: RecipeMaster[];

  constructor() {
    this.recipeMaster = require('./recipeMaster.json');
    // this.recipeMaster = data;
  }

  getAllRecipes() {
    return [...this.recipesArr];
  }

  getRecipe(recipeID: string) {
    return {
      ...this.recipesArr.find(recipe => {
        return recipe.id === recipeID;
      })
    };
  }

  deleteRecipe(recipeID: string) {
    console.log('deleting recipe');
    this.recipesArr = this.recipesArr.filter(recipe => {
      return recipe.id !== recipeID;
    });
  }

  displayRecipeMaster() {
    console.log(this.recipeMaster);
    console.log('$$$$$$');
    console.log(this.recipeMaster[0].name);

    return this.recipeMaster[0].name;
  }

  getAllMasterRecipes() {
    return [...this.recipeMaster];
  }

  getMasterRecipe(recipeID: string) {
    return {
      ...this.recipeMaster.find(recipe => {
        return recipe.id === recipeID;
      })
    };
  }

  deleteMasterRecipe(recipeID: string) {
    console.log('deleting  Master recipe');
    this.recipeMaster = this.recipeMaster.filter(recipe => {
      return recipe.id !== recipeID;
    });
  }
}
