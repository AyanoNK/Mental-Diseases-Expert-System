import { makeStyles } from "@mui/styles";
import { Box } from "@mui/system";
import MainForm from "./MainForm";

const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: theme.palette.background.main,
    width: "100%",
    minHeight: "100vh",
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
