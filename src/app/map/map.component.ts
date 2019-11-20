import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  constructor() { }
  title = 'My first AGM project';
  lat = 51.678418;
  lng = 7.809007;

  ngOnInit() {
  }

}
