import { Component, Input } from '@angular/core';

@Component({
    selector: 'app-users',
    template: `
    <h3> Diff file </h3>
    <p>I'm in the UsersComponent </p>
    <p>Hello {{ name }}  !</p>
    <button (click)="showInfo = true">Show Info </button>
    <p *ngIf="showInfo"> You're a moron! </p>
    <p *ngFor=" let user of users"> {{ user }} </p>
    <p [ngStyle]="{'background-color': color}"> This is Green Mean Machine! </p>
    `
})

export class UsersComponent {
    Kautilya = 'Sensehack';
    name = 'Chanakya';
    showInfo = false;
    color = 'green';
    @Input() users: any;
}
