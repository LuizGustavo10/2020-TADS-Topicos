import { Component } from "@angular/core";

//decorator
@Component({
    selector: "calculadora-salvar",//nome referencial
    templateUrl: "./calcular.componente.html",//arquivo html
    styleUrls: ["./calcular.componente.css"] //arquivo css
})

//classe
export class CalcularImcComponente{
    peso2: number;
    altura2: number;
    imc2: number;

    constructor(){
        this.imc2
    }

    calcularImc2(): number {
        let imc = 0;
        let alt = this.altura2;
        let pes = this.peso2;
        this.imc2 = pes / (alt ** 2);
        alert(this.imc2);
        return this.imc2;
    }
}