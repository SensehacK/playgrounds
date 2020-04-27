import { AngularStateMgtPage } from './app.po';

describe('angular-state-mgt App', function() {
  let page: AngularStateMgtPage;

  beforeEach(() => {
    page = new AngularStateMgtPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
