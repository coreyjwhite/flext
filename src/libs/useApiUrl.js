/**
 * @module useApiUrl
 * @category Utilities
 * @description Concatenates a URL host with the path parameter
 * @param {string} path
 */

import config from "config";

export default function useApiUrl(path) {
  return `${config.apiHost}${path}`;
}
