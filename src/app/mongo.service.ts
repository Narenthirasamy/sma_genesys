import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class MongoService {

  constructor(private httpClient: HttpClient) { }
  private url="../../assets/hi.json"
  public getdata(){
    return this.httpClient.get(this.url);
  }


}
