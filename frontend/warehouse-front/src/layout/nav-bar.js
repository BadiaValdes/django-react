import React from 'react';
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import MenuItem from "@mui/material/MenuItem";
import Button from "@mui/material/Button";
import {pages} from "./layout";

function NavBar(props) {
    return (
        <Box sx={{flexGrow: 1}}>
            <AppBar position="static">
                <Toolbar>
                    <IconButton
                        size="large"
                        edge="start"
                        color="inherit"
                        aria-label="menu"
                        sx={{
                            mr: 2,
                            display: {
                                md: 'none',
                            }
                        }}

                    >
                        <MenuIcon/>
                    </IconButton>
                    <Typography variant="h5" component="div" style={{'padding-right': '12px',}}>
                        Curso Django React
                    </Typography>
                    <Box style={{'display': 'flex', 'flex-direction': 'row', 'flex-grow': '1'}}>
                        {
                            pages.map(page => (
                                <MenuItem key={page} style={{'border-radius': '10px'}}>
                                    <Typography>
                                        {page.title}
                                    </Typography>
                                </MenuItem>
                            ))
                        }
                    </Box>
                </Toolbar>
            </AppBar>
        </Box>
    );
}

export default NavBar;