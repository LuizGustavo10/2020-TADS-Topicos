import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { ObjetivoComponent } from './objetivo/objetivo.component';
import { CalculadoraComponent } from './calculadora/calculadora.component';
import { MediaComponent } from './media/media.component';
// import { HelloWord } from './helloWord/helloWord.component';
import { AppRoutingModule } from './app-routing.module';
import { ClienteModule } from './cliente/cliente.module';
import { CalculadoraImcModule } from './calculadoraImc/calculadoraImc.module';
import { TabelaImcModule } from "./tabelaImc/tabelaImc.module";


@NgModule({
  declarations: [
    AppComponent, ObjetivoComponent, MediaComponent, CalculadoraComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule,
    ClienteModule,
    CalculadoraImcModule,
    TabelaImcModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
