import { SiteAngularPage } from './app.po';

describe('site-angular App', function() {
  let page: SiteAngularPage;

  beforeEach(() => {
    page = new SiteAngularPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
