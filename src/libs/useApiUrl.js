/**
 * @module useApiUrl
 * @category Utilities
 * @description Concatenates a URL host with the path parameter
 * @param {string} path
 */

export default function useApiUrl(path) {
  return `http://192.168.1.77:5000${path}`;
}
