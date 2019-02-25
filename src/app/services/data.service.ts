import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})

export class DataService {
    private message: string;

    constructor() {
        this.message = 'Hello Sensehack';

    }

    getMessage() {
        return this.message;
    }
}
