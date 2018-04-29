import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';
import {createStore} from 'redux';
import reducers from "./reducers";
import {BrowserRouter} from "react-router-dom";
import {Route} from "react-router";

import Login from './pages/Login';
import Welcome from './pages/Welcome';

const store = createStore(reducers);

ReactDOM.render(
    <Provider store={store}>
        <BrowserRouter>
            <div>
                <Route path='/' component={Welcome}/>
                <Route path='/login' component={Login}/>
            </div>
        </BrowserRouter>
    </Provider>,
    document.getElementById('react-app')
);
