import { Component } from "@angular/core";

@Component({
  selector : "calculadora-component",
  templateUrl : "./calculadora.component.html",
  styleUrls : ["./calculadora.component.css"]
})
export class CalculadoraComponent {
 


    value1: number;
    value2: number;
    result: number;

    constructor(){

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

  
}    

