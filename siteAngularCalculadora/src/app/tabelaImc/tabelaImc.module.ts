import { NgModule } from "@angular/core";
import { TabelaComponent } from "./dados-tabela/tabela.component" 

//esse é um módulo filho

//decorator
//metadados
@NgModule({
    declarations : [TabelaComponent],
    exports : [TabelaComponent],//exportações
    imports : [ ]//importações
})
export class TabelaImcModule{

}