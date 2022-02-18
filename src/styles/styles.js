/**
 * @module Styles
 * @category Styling
 * @description Thanks to {@link https://tailwindcss.com/docs/box-shadow|Tailwind CSS}
 * for box shadow values
 */

import c from "styles/color";

const styles = {
  borderRadius: "0.16rem",
  activeBorder: `2px solid ${c.primary5}`,
  activeBorderHidden: "2px solid transparent",
  inactiveBorder: `1px solid ${c.gray7}`,
  inputTransition: "0.2s",
  elev1: "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
  elev2: "0 1px 3px 0 rgb(0 0 0 / 10%), 0 1px 2px 0 rgb(0 0 0 / 6%)",
  elev3:
    "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
  elev4:
    "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
  elev5:
    "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"
};

export default styles;
