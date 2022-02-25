import styled from "styled-components";
import m from "styles/measures";
import s from "styles/styles";

const StyledDiv = styled.div.attrs((props) => ({
  id: `${props.label}Space`,
  className: "space",
}))`
  display: flex;
  width: ${m.sp14};
  height: ${m.sp12};
  align-items: center;
  justify-content: center;
  margin: ${m.sp6};
  box-shadow: ${(props) => props.elevation};
`;

export default function Elevations() {
  return (
    <div style={{ display: "flex", flexDirection: "row" }}>
      <StyledDiv label="Elevation 1" elevation={s.elev1}>
        <p>1</p>
      </StyledDiv>
      <StyledDiv label="Elevation 2" elevation={s.elev2}>
        <p>2</p>
      </StyledDiv>
      <StyledDiv label="Elevation 3" elevation={s.elev3}>
        <p>3</p>
      </StyledDiv>
      <StyledDiv label="Elevation 4" elevation={s.elev4}>
        <p>4</p>
      </StyledDiv>
      <StyledDiv label="Elevation 5" elevation={s.elev5}>
        <p>5</p>
      </StyledDiv>
    </div>
  );
}
