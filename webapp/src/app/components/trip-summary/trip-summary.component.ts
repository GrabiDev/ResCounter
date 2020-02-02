import { Component, OnInit, ViewChild } from '@angular/core';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import {formatDate} from '@angular/common'

export interface TravelEntry {
  departure: Date;
  arrival: Date;
  description: string;
  time_out: number;
  allowable_absence: number;
}

let getNoOfDays = (departure_date: Date, arrival_date: Date): number => {
  let miliseconds = departure_date.valueOf() - arrival_date.valueOf();
  let seconds = miliseconds/1000;
  let minutes = seconds/60;
  let hours = minutes/60;
  let days = hours/24

  return days - 1; // -1 to comply with Home Office rules
}


let example_departure = new Date(2018, 12, 19);
let example_arrival = new Date(2018, 12, 28);

const TRAVEL_DATA: TravelEntry[] = [
  {departure: example_departure, arrival: example_arrival, description: 'christmas', time_out: getNoOfDays(example_arrival, example_departure), allowable_absence: 180}
];

@Component({
  selector: 'app-trip-summary',
  templateUrl: './trip-summary.component.html',
  styleUrls: ['./trip-summary.component.css']
})
export class TripSummaryComponent implements OnInit {
  displayedColumns: string[] = ['departure', 'arrival', 'description', 'time_out', 'allowable_absence'];
  dataSource = new MatTableDataSource(TRAVEL_DATA);

  constructor() { }

  @ViewChild(MatSort, {static: true}) sort: MatSort;

  ngOnInit() {
    this.dataSource.sort = this.sort;
  }

  formatDate(date: Date) {
    return formatDate(date, 'd MMMM y', 'en-GB')
  }

}
