import React from "react";

import styled from 'styled-components';

export default class Welcome extends React.Component {
    render() {
        return (
            <SiteName>Hello world</SiteName>
        );
    }
}

const SiteName = styled.h1`
    font-size: 40px;
`;
