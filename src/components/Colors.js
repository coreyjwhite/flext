/**
 * @module Palette
 */

import styled from "styled-components";
import camelize from "libs/camelize";
import c from "styles/color";
import m from "styles/measures";
import s from "styles/styles";

const ColorSwatch = styled.div.attrs((props) => ({
  id: `${props.data}ColorSwatch`,
  className: "colorSwatch",
}))`
  width: ${m.sp7};
  min-height: ${m.sp7};
  margin: ${m.sp2};
  background: ${(props) => props.bg};
  border-radius: ${s.borderRadius};
  box-shadow: ${s.elev1};
  @media (min-width: ${m.devMd}) {
    width: ${m.sp8};
    min-height: ${m.sp8};
  }
`;

const LabelContainer = styled.div.attrs({
  id: "labelContainer",
})`
  display: flex;
  width: fit-content;
  flex-direction: column;
  align-items: flex-end;
  justify-content: space-between;
  margin-right: ${m.sp3};
  p {
    height: ${m.sp7};
    margin: ${m.sp2};
  }
`;

const PaletteContainer = styled.div.attrs({
  id: "paletteContainer",
})`
  display: flex;
  margin: ${m.sp4};
`;

const SwatchContainer = styled.div.attrs({
  id: "swatchContainer",
})`
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
`;

const SwatchRow = styled.div.attrs((props) => ({
  id: `${camelize(props.label)}SwatchRow`,
}))`
  display: flex;
  justify-content: flex-start;
  text-align: center;
  p {
    width: ${m.sp7};
    height: ${m.sp7};
    margin: ${m.sp2};
    vertical-align: middle;
    @media (min-width: ${m.devMd}) {
      width: ${m.sp8};
    }
  }
`;

// iterate over properties to find unique substrings
function getStyleCategories(propNames) {
  const styleCategories = [];
  propNames.forEach(function (name) {
    name = name.replace(/[0-9]/g, "");
    if (!styleCategories.includes(name)) {
      styleCategories.push(name);
    }
  });
  return styleCategories;
}

// iterate over properties to find names matching category
function getCategoryProps(category, css) {
  const propNames = Object.keys(css);
  const categoryProps = [];
  propNames.forEach(function (key) {
    if (key.includes(category)) {
      return categoryProps.push(key);
    }
  });
  return categoryProps;
}

// iterate over category colors and return a ColorSwatch for each
function categoryCards(obj) {
  const categoryProps = getCategoryProps(obj, c);
  return (
    <SwatchRow label={obj} key={obj} data={obj}>
      {categoryProps.map(function (prop) {
        return <ColorSwatch key={prop} bg={c[prop]} data={prop} />;
      })}
    </SwatchRow>
  );
}

export default function Colors() {
  const propNames = Object.keys(c);
  const styleCategories = getStyleCategories(propNames);
  return (
    <>
      <PaletteContainer>
        <LabelContainer>
          <SwatchRow label="Color Labels Header">
            <p key=""></p>
          </SwatchRow>
          {styleCategories.map(function (cat, key) {
            return (
              <p key={key} data={key}>
                {cat}
              </p>
            );
          })}
        </LabelContainer>
        <SwatchContainer>
          <SwatchRow label="Swatch Headers">
            <p>1</p>
            <p>2</p>
            <p>3</p>
            <p>4</p>
            <p>5</p>
            <p>6</p>
            <p>7</p>
            <p>8</p>
            <p>9</p>
          </SwatchRow>
          {styleCategories.map(function (cat) {
            return categoryCards(cat);
          })}
        </SwatchContainer>
      </PaletteContainer>
    </>
  );
}
