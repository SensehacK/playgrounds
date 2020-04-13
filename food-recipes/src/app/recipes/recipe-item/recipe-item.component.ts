import { Component, OnInit, Input } from '@angular/core';
import { RecipeMaster } from '../recipeMaster.model';

@Component({
  selector: 'app-recipe-item',
  templateUrl: './recipe-item.component.html',
  styleUrls: ['./recipe-item.component.scss'],
})
export class RecipeItemComponent implements OnInit {

  @Input() recipeItem: RecipeMaster;

  constructor() { }

  ngOnInit() {}

}
