/**
 * @module Global
 * @category Styling
 */

import { createGlobalStyle } from "styled-components";
import c from "styles/color";
import s from "styles/styles";

const global = createGlobalStyle`

  // general styles
  html,
  body {
    background-color: ${c.gray9};
  }

  a {
    color: inherit;
  }

  p, h1, h2, h3, h4, h5, h6, td {
    color: ${c.gray2};
  }

  p.light {
    font-weight: 200;
    color: ${c.gray6};
  }

  p.bold {
    font-weight: 600;
  }

  p.italic {
    font-style: italic
  }

  *::selection{
    color: ${c.primary9};
  }

  * {
    box-sizing: border-box;
    image-rendering: -webkit-optimize-contrast;
  }


  *.swagger-ui {
    width: 75%;
  }

}`;
export default global;
