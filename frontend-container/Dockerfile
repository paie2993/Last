FROM node:latest

RUN [ "npm", "init", "react-app", "frontend" ]

WORKDIR /frontend/

RUN [ "npm", "install", "@fontsource/roboto" ]
RUN [ "npm", "install", "@mui/material" ]
RUN [ "npm", "install", "@mui/icons-material" ]
RUN [ "npm", "install", "@mui/lab" ]
RUN [ "npm", "install", "@mui/styled-engine-sc", "styled-components" ]
RUN [ "npm", "install", "@emotion/react", "@emotion/styled" ]
RUN [ "npm", "install", "react-router-dom" ]

RUN rm ./src/*

COPY [ "./source/", "./src/" ]

ENTRYPOINT [ "npm", "start" ]
