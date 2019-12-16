import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { QuotePage } from './quote.page';

describe('QuotePage', () => {
  let component: QuotePage;
  let fixture: ComponentFixture<QuotePage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ QuotePage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(QuotePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
