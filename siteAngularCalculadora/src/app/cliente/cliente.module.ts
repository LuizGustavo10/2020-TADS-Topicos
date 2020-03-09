import { NgModule } from "@angular/core";
import { SalvarComponente } from "./cliente-salvar/salvar.componente";
import { CalcularImcComponente } from "../calculadoraImc/calculadora-salvar/calcular.componente";
import { FormsModule } from '@angular/forms';

@NgModule({
    declarations: [SalvarComponente],
    exports: [SalvarComponente], //componentes exportados
    imports: [FormsModule] //componentes utilizados
})

export class ClienteModule{

}

