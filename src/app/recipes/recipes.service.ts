import { Injectable } from '@angular/core';
import { Recipe } from './recipe.model';

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
    }
  ];

  constructor() {}

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
}
