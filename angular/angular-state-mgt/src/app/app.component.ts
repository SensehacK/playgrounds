import { Component } from '@angular/core';
import { Store } from '@ngrx/store';
import { Observable } from 'rxjs/Observable';

interface AppState {
  message: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Hello Sensehack!';

  message$: Observable<string>

  constructor(private store: Store<AppState>) {
    this.message$ = this.store.select('message');
    this.store.dispatch({type: 'MARATHI'});
  }

  marathiMessage() {
    this.store.dispatch({type: 'MARATHI'});
  }

  frenchMessage() {
    this.store.dispatch({type: 'FRENCH'});
  }
}
