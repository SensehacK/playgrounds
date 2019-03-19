import { Component, OnInit } from '@angular/core';
import { Recipe } from './recipe.model';

@Component({
  selector: 'app-recipes',
  templateUrl: './recipes.page.html',
  styleUrls: ['./recipes.page.scss']
})
export class RecipesPage implements OnInit {
  recipesArr: Recipe[] = [
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

  ngOnInit() {}
}
