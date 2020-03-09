import { Component } from "@angular/core";

@Component({
  selector : "objetivo-component",
  templateUrl : "./objetivo.component.html",
  styleUrls : ["./objetivo.component.css"]
})
export class ObjetivoComponent {
    disciplina: String ="POO";
    soma : number = 0;
    nome : string = "";
    data : number = 0;
    //nascimento : number = this.data.getFullYear();

    peso: number;
    altura: number;
    imc: number;

    value1: number;
    value2: number;
    result: number;

    nota1: number;
    nota2: number;
    nota3: number;
    nota4: number;
    totalMedia: number;

    //operacao: string;

    constructor(){
      this.disciplina = "DDM";

      //this.soma = this.calcular(5,5);
      //this.soma = somar(num1: number, num2: number);
    }

    calcular(num1: number, num2:number) : number {
      let total = 0;
      total = num1 + num2;
      return total;
    }
    subtrair():void{

    }
    hello():void{
      let anoAtual = new Date().getFullYear();
      let idade = anoAtual - this.data;
      alert("Hello word "+ idade + anoAtual);
      //fazer calculadora e media aritmetica, atenção isso anulará a prova 
    }
    somar(): number {
      let tot =0;
      let num1 = this.value1;
      let num2 = this.value2;
      this.result = num1 + num2;
      alert(this.result);
      return this.result;
    }
    sub(): number {
      let tot = 0;
      let num1 = this.value1;
      let num2 = this.value2;
      this.result = num1 - num2;
      alert(this.result);
      return this.result;
    }
    div(): number {
      let tot = 0;
      let num1 = this.value1;
      let num2 = this.value2;
      this.result = num1 / num2;
      alert(this.result);
      return this.result;
    }
    mult(): number {
      let tot = 0;
      let num1 = this.value1;
      let num2 = this.value2;
      this.result = num1 * num2;
      alert(this.result);
      return this.result;
    }

    //---------------------------------

    media(): number {
      let tot = 0;
      let num1 = this.nota1;
      let num2 = this.nota2;
      let num3 = this.nota3;
      let num4 = this.nota4;
      this.totalMedia = (num1 + num2 + num3 + num4) / 4;
      alert(this.totalMedia);
      return this.totalMedia;
    }

  calcularImc(): number {
    let imc = 0;
    let alt = this.altura;
    let pes = this.peso;
    this.imc = pes / (alt ** 2);
    alert(this.imc);
    return this.imc;
  }


  
  
}    

