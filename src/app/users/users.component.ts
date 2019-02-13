import { Component } from '@angular/core';

@Component({
    selector: 'app-users',
    template: `
    <h3> Diff file </h3>
    <p>I'm in the UsersComponent </p>
    <p>Hello {{ name }}  !</p>
    `
})

export class UsersComponent {
    Kautilya = 'Sensehack';
    name = 'Chanakya';
}
