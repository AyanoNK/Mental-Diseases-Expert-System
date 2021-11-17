import { createTheme } from "@mui/material/styles";
import { red } from "@mui/material/colors";
import "@fontsource/m-plus-1p";

// A custom theme for this app
const theme = createTheme({
  typography: {
    fontFamily: `"M PLUS 1p"`,
    fontSize: 14,
    fontWeightLight: 300,
    fontWeightRegular: 400,
    fontWeightMedium: 500,
  },
  palette: {
    primary: {
      main: "#EFC88B",
    },
    secondary: {
      main: "#CF5C36",
    },
    error: {
      main: red.A400,
    },
    grey: "#7C7C7C",
    black: {
      main: "#000000",
    },
    background: {
      main: "#EEE5E9",
    },
  },
});

export default theme;
