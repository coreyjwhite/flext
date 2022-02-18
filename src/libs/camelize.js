/**
 * @module camelize
 * @category Utilities
 * @description Converts a string to camelCase
 * @param {string} str
 */

export default function camelize(str) {
  if (str == undefined) {
    return undefined;
  } else {
    return str
      .replace(/(?:^\w|[A-Z]|\b\w)/g, function(word, index) {
        return index === 0 ? word.toLowerCase() : word.toUpperCase();
      })
      .replace(/\s+/g, "");
  }
}
