import "../styles/globals.css";
import type { AppProps } from "next/app";
import { Provider as NextAuthProvider } from "next-auth/client";

// material ui
import {
  ThemeProvider,
  Theme,
  StyledEngineProvider,
} from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import createCache from "@emotion/cache";
import { CacheProvider } from "@emotion/react";
import theme from "@libs/theme";

const materialUiCache = createCache({ key: "css", prepend: true });
materialUiCache.compat = true;

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <NextAuthProvider session={pageProps}>
      <CacheProvider value={materialUiCache}>
        <StyledEngineProvider injectFirst>
          <ThemeProvider theme={theme}>
            <CssBaseline />
            <Component {...pageProps} />
          </ThemeProvider>
        </StyledEngineProvider>
      </CacheProvider>
    </NextAuthProvider>
  );
}
export default MyApp;