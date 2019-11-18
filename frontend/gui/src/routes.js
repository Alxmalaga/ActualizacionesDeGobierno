import React from 'react';
import { Route } from 'react-router-dom';

import RegionList from './containers/RegionListView';
import RegionDetail from './containers/RegionDetailView';
import PoliticianDetail from './containers/PoliticianDetailView';



const BaseRouter = () => (
    <div>
        <Route exact path='/' component={RegionList} />
        <Route exact path='/regions/:regionID' component={RegionDetail} />
        <Route exact path='/politicians/:politicianID' component={PoliticianDetail} />
    </div>

);

export default BaseRouter;
