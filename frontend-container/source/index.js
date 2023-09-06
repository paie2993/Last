import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Dashboard from './Dashboard';
import TitlesList from './TitleList';
import TextPage from './TextPage';
import Dictionary from './Dictionary';
import './index.css'
import UserDictionary from './UserDictionary';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Dashboard />} >
          <Route index element={<TitlesList />} />
          <Route path='/texts/content/:title' element={<TextPage />} />
          <Route path='/dictionary' element={<Dictionary />} />
          <Route path='/user/dictionary' element={<UserDictionary />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode >
);