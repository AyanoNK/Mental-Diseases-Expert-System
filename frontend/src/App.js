import { makeStyles } from "@mui/styles";
import { Box } from "@mui/system";
import MainForm from "./MainForm";

/*
Palette: {
  black: #000000,
  flame: #CF5C36, 
  lavender: #EEE5E9, this is background
  gray: #7C7C7C,
  gold: #EFC88B
}
*/

const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: theme.palette.background.main,
    width: "100%",
    height: "100vh",
    position: "absolute",
  },
}));

const App = () => {
  const classes = useStyles();
  return (
    <Box className={classes.root}>
      <MainForm />
    </Box>
  );
};

export default App;
