import { Component, OnInit } from '@angular/core';
import {MongoService} from '../mongo.service'


@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css'],
  //template:'<h2>  Map Chart</h2><div id="map_chart" [chartData]="map_ChartData" [chartOptions] = "map_ChartOptions" chartType="GeoChart" GoogleChart></div>'
})
export class PostsComponent implements OnInit {
private a;
  constructor(private service:MongoService) { }


  ngOnInit() {

    this.service.getdata().subscribe((data)=>{
      console.log(data)
      this.a = data
    })
  }

}
