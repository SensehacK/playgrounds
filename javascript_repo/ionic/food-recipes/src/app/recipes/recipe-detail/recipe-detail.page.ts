import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { RecipesService } from '../recipes.service';
import { Recipe } from '../recipe.model';
import { AlertController } from '@ionic/angular';
import { RecipeMaster } from '../recipeMaster.model';

@Component({
  selector: 'app-recipe-detail',
  templateUrl: './recipe-detail.page.html',
  styleUrls: ['./recipe-detail.page.scss']
})
export class RecipeDetailPage implements OnInit {
  loadedRecipe: Recipe;
  recipeID: string;
  recipeMasterName: string;
  recipeMaster: RecipeMaster[];
  loadedRecipeMaster: RecipeMaster;

  constructor(
    private activatedRoute: ActivatedRoute,
    private recipeService: RecipesService,
    private router: Router,
    private alertCtrl: AlertController
  ) {}

  ngOnInit() {
    this.activatedRoute.paramMap.subscribe(paramMap => {
      if (!paramMap.has('recipeID')) {
        // redirect user
      }

      this.recipeID = paramMap.get('recipeID');
      console.log('Recipe ID ', this.recipeID);
      this.loadedRecipe = this.recipeService.getRecipe(this.recipeID);

      // MAster Recipe JSON data
      this.recipeMasterName = this.recipeService.displayRecipeMaster();

      this.recipeMaster = this.recipeService.getAllMasterRecipes();
      // calling specific object for recipe
      this.loadedRecipeMaster = this.recipeService.getMasterRecipe(
        this.recipeID
      );
    });
  }

  onDeleteRecipe() {
    this.alertCtrl
      .create({
        header: 'Kautilya',
        subHeader: 'Are you Sure?',
        message: 'Do you really want to delete the recipe?',
        buttons: [
          {
            text: 'Cancel',
            role: 'cancel'
          },
          {
            text: 'Delete',
            handler: () => {
              // Old recipe data call
              this.recipeService.deleteRecipe(this.recipeID);
              // new recipe data call
              this.recipeService.deleteMasterRecipe(this.recipeID);
              this.router.navigate(['/recipes']);
            }
          }
        ]
      })
      .then(alertEl => {
        alertEl.present();
      });
  }
}
