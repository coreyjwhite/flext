/**
 * @module _app
 * @description Base Next.js _app file
 */

import PropTypes from "prop-types";
import Head from "next/head";
import { Normalize } from "styled-normalize";
import { QueryClient, QueryClientProvider } from "react-query";
import GlobalStyle from "styles/global";
import pkg from "/package.json";

const fetcher = (...args) => fetch(...args).then((res) => res.json());
const queryClient = new QueryClient();

export default function App({ Component }) {
  return (
    <>
      <Normalize />
      <GlobalStyle />
      <QueryClientProvider client={queryClient}>
        <Head>
          <link rel="icon" />
          <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0, viewport-fit=cover"
          />
          <meta name="author" content={pkg.author.name} />
        </Head>
        <Component />
      </QueryClientProvider>
    </>
  );
}

App.propTypes = {
  Component: PropTypes.elementType,
};
