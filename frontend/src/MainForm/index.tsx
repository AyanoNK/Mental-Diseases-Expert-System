import { Card, CardContent, Grid, Typography } from "@mui/material";
import { makeStyles } from "@mui/styles";
import { Box } from "@mui/system";
import React, { FC } from "react";
import Form from "./Form";

type Props = {};

const useStyles = makeStyles((theme: any) => ({
  root: {},
  card: {
    minHeight: "80vh",
  },
}));

const MainForm: FC<Props> = (props) => {
  const classes = useStyles();
  return (
    <Box className={classes.root}>
      <Box mt={2} mb={5}>
        <Grid container justifyContent="center">
          <Grid item xs={12}>
            <Typography align="center" variant="h3">
              Sistema Experto
            </Typography>
          </Grid>
        </Grid>
      </Box>
      <Grid container justifyContent="center">
        <Grid item xs={6} mb={5}>
          <Card className={classes.card}>
            <CardContent>
              <Form />
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
};

export default MainForm;
