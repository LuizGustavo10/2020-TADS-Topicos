import { Component } from "@angular/core";

@Component({
  selector : "media-component",
  templateUrl : "./media.component.html",
  styleUrls : ["./media.component.css"]
})
export class MediaComponent {

    nota1: number;
    nota2: number;
    nota3: number;
    nota4: number;
    totalMedia: number;

    //operacao: string;

    constructor(){
     
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


  
  
}    

