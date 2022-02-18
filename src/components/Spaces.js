/**
 * @module Spaces
 */

import PropTypes from "prop-types";
import styled, { keyframes } from "styled-components";
import c from "styles/color";
import m from "styles/measures";
import s from "styles/styles";

const growRight = keyframes`
  from {
      transform: scale(0, 1);
  }
  to {
      transform: scale(1, 1);
  }
`;

const SpaceBar = styled.div.attrs((props) => ({
  id: `${props.label}Space`,
  className: "space",
}))`
  display: inline-block;
  width: ${(props) => props.width};
  height: ${m.sp5};
  margin-top: ${m.sp6};
  animation: ${growRight} 2s linear;
  background: ${c.warning1};
  border-radius: ${s.borderRadius};
  box-shadow: ${s.elev2};
  transform-origin: 0% 100%;
`;

const SpacesContainer = styled.div.attrs((props) => ({
  id: "spacesContainer",
}))`
  width: ${m.col12};
  flex-direction: column;
  overflow-x: scroll;
  p {
    display: inline;
    min-width: ${m.sp10};
    margin: ${m.sp4} 0;
  }
  p.header {
    margin: 0;
    text-decoration: underline;
  }
  p.key {
    min-width: ${m.sp9};
    font-weight: 600;
    text-align: right;
  }
  p.value {
    font-style: italic;
    text-align: center;
  }
`;

// iterate over properties to find "sp"
function getSpaceKeys(measures) {
  const spaces = [];
  measures.forEach(function (key) {
    if (key.startsWith("sp")) {
      spaces.push(key);
    }
  });
  return spaces;
}

// iterate over category colors and return a Space for each
function getSpaceValues(spaces) {
  const values = [];
  Object.keys(m).forEach(function (key) {
    if (spaces.includes(key)) {
      var obj = {};
      obj.key = key;
      obj.value = m[key];
      return values.push(obj);
    }
  });
  return values;
}

export default function Spaces(props) {
  const measures = Object.keys(m);
  const values = getSpaceValues(getSpaceKeys(measures));
  return (
    <SpacesContainer label="Spaces" showHeading={true} width={props.width}>
      <div
        label="Spaces Labels Header"
        justify="flex-start"
        width="fit-content"
        style={{ flexWrap: "nowrap" }}
      >
        <p className="key header">key</p>
        <p className="value header">rem</p>
      </div>
      {values.map(function (cat) {
        return (
          <div
            key={cat.key}
            label={`${cat.key} Label`}
            justify="flex-start"
            width="fit-content"
            style={{ flexWrap: "nowrap" }}
          >
            <p className="key">{cat.key}</p>
            <p className="value">{cat.value.replace("rem", "")}</p>
            <SpaceBar label={cat.key} width={cat.value} />
          </div>
        );
      })}
    </SpacesContainer>
  );
}

Spaces.propTypes = {
  width: PropTypes.string,
};
