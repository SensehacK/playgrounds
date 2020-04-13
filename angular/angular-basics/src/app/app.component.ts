import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Kautilya Works!';
  awesome = 'Just Kidding';
  age = 99;
  person = {
    name: 'Ks',
    age: 66
  };

  RegUsers = ['KL', 'RL', 'TY'];

  getName() {
    return 'K$';
  }

  getRickRolled() {
    const url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ';
    return url;
  }

  setAge() {
    this.age = 102;
  }

  setPersonAge(age: number) {
    this.person.age = age;
  }
}
