import { Action } from '@ngrx/store';

export function simpleReducer(state: string = 'Hello World', action: Action) {
  console.log('In reducer of function');
  console.log(action.type, state);

  switch (action.type) {
    case 'MARATHI':
      return state = 'Namaskar Vishwa';

    case 'FRENCH':
      return state = 'Bonjour le monde';

    default:
      return state;

  }
}
