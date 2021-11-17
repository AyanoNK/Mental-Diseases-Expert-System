import { Button, Grid, Typography } from "@mui/material";
import { makeStyles } from "@mui/styles";
import React, { FC, useEffect, useState } from "react";

const useStyles = makeStyles((theme) => ({
  root: {},
}));

type Props = {
  questionText: string;
  question: string;
  setOptions: (prevState: any) => void;
};
const Question: FC<Props> = ({ questionText, question, setOptions }) => {
  const classes = useStyles();
  const [answer, setAnswer] = useState<boolean | null>(null);

  useEffect(() => {
    if (answer !== null) {
      setOptions((prevState: any) => ({
        ...prevState,
        [question]: answer,
      }));
    }
  }, [answer, question, setOptions]);

  const handleButton = (ans: boolean) => {
    setAnswer(ans);
  };

  return (
    <Grid container direction="column" className={classes.root}>
      <Grid item xs={12}>
        <Typography variant="h6" align="center">
          {questionText}
        </Typography>
      </Grid>
      <Grid item xs={12}>
        <Grid container direction="row" justifyContent="center" spacing={2}>
          <Grid item xs={6}>
            <Button onClick={() => handleButton(false)}>
              <Typography variant="body1">No</Typography>
            </Button>
          </Grid>
          <Grid item xs={6}>
            <Button onClick={() => handleButton(true)}>
              <Typography variant="body1">Sí</Typography>
            </Button>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default Question;
