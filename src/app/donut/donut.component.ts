import { Component, OnInit } from '@angular/core';
import { ChartType } from 'chart.js';
import { MultiDataSet, Label ,Color} from 'ng2-charts';


@Component({
  selector: 'app-donut',
  templateUrl: './donut.component.html',
  styleUrls: ['./donut.component.css']
})
export class DonutComponent implements OnInit {


  public doughnutChartLabels: Label[] = ['Positive','Negative','Nuetral'];
  public doughnutChartData: MultiDataSet = [
    [350, 450, 100],
  ];
 
  public lineChartColors: Color[] =[ { 
    backgroundColor: ['#38CF0A ', 'red', '#F1C40F']
  }]
  public doughnutChartType: ChartType = 'doughnut';
  constructor() { }

  ngOnInit() {
  }

   // events
   public chartClicked({ event, active }: { event: MouseEvent, active: {}[] }): void {
    console.log(event, active);
  }

  public chartHovered({ event, active }: { event: MouseEvent, active: {}[] }): void {
    console.log(event, active);
  }
}
