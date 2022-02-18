/**
 * @module useRequest
 * @category Utilities
 * @description Wrapper for useQuery that concatenates the API url from
 * config.js with the parameter path
 * @param {string} path
 */

import { useQuery } from "react-query";
import useApiUrl from "libs/useApiUrl";

export default function useRequest(key, path, body = null) {
  if (!path) {
    throw new Error("Path is required");
  }

  const url = useApiUrl(path);
  const { isLoading, error, data } = useQuery(key, async () =>
    fetch(url, body && { body: JSON.stringify(body) }).then(res => res.json())
  );

  return { data, error, isLoading };
}
