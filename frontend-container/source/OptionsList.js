import * as React from 'react';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import CollectionsBookmarkIcon from '@mui/icons-material/CollectionsBookmark';
import LocalLibraryIcon from '@mui/icons-material/LocalLibrary';
import AutoStoriesIcon from '@mui/icons-material/AutoStories';
import { Link } from 'react-router-dom';

export const optionsList = (
  <React.Fragment>
    <Link to={'/'}>
      <ListItemButton>
        <ListItemIcon>
          <CollectionsBookmarkIcon />
        </ListItemIcon>
        <ListItemText primary="Texts" />
      </ListItemButton>
    </Link>
    <Link to={'/dictionary'}>
      <ListItemButton>
        <ListItemIcon>
          <AutoStoriesIcon />
        </ListItemIcon>
        <ListItemText primary="Dictionary" />
      </ListItemButton>
    </Link>
    <Link to={'/user/dictionary'}>
      <ListItemButton>
        <ListItemIcon>
          <LocalLibraryIcon />
        </ListItemIcon>
        <ListItemText primary="My Dictionary" />
      </ListItemButton>
    </Link>
  </React.Fragment>
);