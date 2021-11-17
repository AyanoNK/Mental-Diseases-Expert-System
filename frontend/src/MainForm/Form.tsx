import { Grid } from "@mui/material";
import React, { FC, useState } from "react";
import Question from "./Question";

type Props = {};
type Questions = {
  question_1: boolean | null;
  question_2: boolean | null;
  question_3: boolean | null;
  question_4: boolean | null;
  question_5: boolean | null;
  question_6: boolean | null;
  question_7: boolean | null;
  question_8: boolean | null;
  question_9: boolean | null;
  question_10: boolean | null;
  question_11: boolean | null;
  question_12: boolean | null;
};
const Form: FC<Props> = () => {
  const [options, setOptions] = useState<Questions>({
    question_1: null,
    question_2: null,
    question_3: null,
    question_4: null,
    question_5: null,
    question_6: null,
    question_7: null,
    question_8: null,
    question_9: null,
    question_10: null,
    question_11: null,
    question_12: null,
  });
  console.log(options);
  const onSubmit = () => {};

  return (
    <Grid container justifyContent="center">
      <form onSubmit={onSubmit}>
        <Grid item xs={12}>
          <Question
            questionText="¿Tienes delirios mentales?"
            question="question_1"
            setOptions={setOptions}
          />
        </Grid>
      </form>
    </Grid>
  );
};

export default Form;
