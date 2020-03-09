import { NgModule } from "@angular/core";
import { CalcularImcComponente } from "./calculadora-salvar/calcular.componente"

import { FormsModule } from '@angular/forms';

@NgModule({
        
    declarations: [CalcularImcComponente],
    exports: [CalcularImcComponente], //componentes exportados
    imports: [ FormsModule] //componentes utilizados
})

export class CalculadoraImcModule{
   
}