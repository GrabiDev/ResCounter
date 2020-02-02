import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TripSummaryComponent } from './components/trip-summary/trip-summary.component';


const routes: Routes = [
  { path: '', component: TripSummaryComponent, pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
