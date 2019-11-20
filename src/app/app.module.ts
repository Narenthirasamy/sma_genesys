import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MaterialModuleModule } from './material-module/material-module.module';
import { SidenavComponent } from './sidenav/sidenav.component';
import { ToolbarComponent } from './toolbar/toolbar.component';
import { GridComponent } from './grid/grid.component';
import { GraphComponent } from './graph/graph.component';

import { ChartsModule } from 'ng2-charts';
import { DonutComponent } from './donut/donut.component';
import { SentimentComponent } from './sentiment/sentiment.component';
import { PostsComponent } from './posts/posts.component';
import { TrendComponent } from './trend/trend.component';
import { PredictionComponent } from './prediction/prediction.component';
import { MapComponent } from './map/map.component';
import { AgmCoreModule } from '@agm/core';




@NgModule({
  declarations: [
    AppComponent,
    SidenavComponent,
    ToolbarComponent,
    GridComponent,
    GraphComponent,
    DonutComponent,
    SentimentComponent,
    PostsComponent,
    TrendComponent,
    PredictionComponent,
    MapComponent,
   
   
   
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModuleModule,
    ChartsModule,
    HttpClientModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyDR28s78zMCqG2JxmQQl-6rZH-K8dzCZ2g'
    })
 
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
