/**
 * @module Palette
 */

import styled from "styled-components";
import camelize from "libs/camelize";
import c from "styles/color";
import m from "styles/measures";
import s from "styles/styles";

const StyledHeading = styled.h1.attrs((props) => ({
  id: `${props.label}Space`,
  className: "space",
}))`
  color: ${c.primary5};
`;

export default function Heading(props) {
  return <StyledHeading>{props.children}</StyledHeading>;
}
