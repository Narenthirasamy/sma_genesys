import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SidenavComponent } from './sidenav/sidenav.component';
import { SentimentComponent } from './sentiment/sentiment.component';
import { PostsComponent } from './posts/posts.component';
import { GridComponent } from './grid/grid.component';
import { PredictionComponent } from './prediction/prediction.component';
import { MapComponent } from './map/map.component';



const routes: Routes = [
{path:"sentiment" , component:SentimentComponent},
{path:"post" , component:PostsComponent},
{path:"prediction" , component:PredictionComponent},
{path:"map" , component:MapComponent},
{path:"**" , component:GridComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
