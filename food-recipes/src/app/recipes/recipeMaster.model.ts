export interface RecipeMaster {
  id: string;
  name: string;
  ingredients: Ingredient[];
  steps: string[];
  timers: number[];
  imageURL: string;
  originalURL?: string;
}

export interface Ingredient {
  quantity: string;
  name: string;
  type: Type;
}

export enum Type {
  Baking = 'Baking',
  Condiments = 'Condiments',
  Dairy = 'Dairy',
  Drinks = 'Drinks',
  Meat = 'Meat',
  Misc = 'Misc',
  Produce = 'Produce'
}
