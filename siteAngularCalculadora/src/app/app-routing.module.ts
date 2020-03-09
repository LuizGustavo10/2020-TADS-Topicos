import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ObjetivoComponent } from "./objetivo/objetivo.component";
import { CalculadoraComponent } from "./calculadora/calculadora.component";
import { MediaComponent } from "./media/media.component";
// import { HelloComponent } from "./helloWord/helloWord.component";

const routes: Routes = [
  {path:"objetivo", component: ObjetivoComponent},
  {path:"calculadora", component: CalculadoraComponent},
  {path: "media", component: MediaComponent },
  // {path:"helloWord", component: HelloWordComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
