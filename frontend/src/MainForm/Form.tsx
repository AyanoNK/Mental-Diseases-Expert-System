import { Grid, Typography } from "@mui/material";
import React, { FC, useEffect, useState } from "react";
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

  const [response, setResponse] = useState<any>(null);

  const onSubmit = async () => {
    await fetch("https://b6cb-190-27-101-255.ngrok.io/")
      .then((response) => setResponse(response))
      .catch((error) => setResponse(error));
  };

  useEffect(() => {
    if (options.question_1 === false) {
      onSubmit();
    }
  }, [options]);

  return (
    <Grid container justifyContent="center">
      <form onSubmit={onSubmit}>
        <Grid item xs={12}>
          <Question
            questionText="¿Presenta delirios, alucinaciones, habla incoherente, tiene comportamiento gravemente desorganizado, y
            síntomas negativos?"
            question="question_1"
            setOptions={setOptions}
          />
        </Grid>
        {options.question_1 && (
          <Grid item xs={12}>
            <Question
              questionText="¿Son derivados directamente de los efectos fisiológicos de una condición médica?"
              question="question_2"
              setOptions={setOptions}
            />
          </Grid>
        )}
        <Grid item xs={12}>
          <Question
            questionText="¿Son derivados directamente de los efectos de una sustancia (medicación, drogas ilícitas, toxinas)?"
            question="question_3"
            setOptions={setOptions}
          />
        </Grid>
        <Grid item xs={12}>
          <Question
            questionText="¿Cumple con los criterios asociados a la esquizofrenia A durante un mes de funcionamiento?"
            question="question_4"
            setOptions={setOptions}
          />
        </Grid>
        <Grid item xs={12}>
          <Question
            questionText="¿Tiene delirios comunes durante un mes?"
            question="question_5"
            setOptions={setOptions}
          />
        </Grid>
        <Grid item xs={12}>
          <Question
            questionText="¿Tiene delirios comunes más de un día y menos de un mes?"
            question="question_6"
            setOptions={setOptions}
          />
        </Grid>
        <Grid item xs={12}>
          <Question
            questionText="¿Tiene manía o depresión mayor con psicósis?"
            question="question_7"
            setOptions={setOptions}
          />
        </Grid>
        <Grid item xs={12}>
          <Question
            questionText="¿Cumple con los criterios asociados a la esquizofrenia A durante seis meses de duración?"
            question="question_8"
            setOptions={setOptions}
          />
        </Grid>
        <Grid item xs={12}>
          <Question
            questionText="¿Todos los periodos de episodios anímicos son breves en comparación con los relacionados con la psicosis?"
            question="question_9"
            setOptions={setOptions}
          />
        </Grid>
        <Grid item xs={12}>
          <Question
            questionText="¿Presenta dos semanas de psicosis positiva sin problemas aníminos prominentes?"
            question="question_10"
            setOptions={setOptions}
          />
        </Grid>
        <Grid item xs={12}>
          <Question
            questionText="¿Presenta episodios anímicos breves comparados con los delirios?"
            question="question_11"
            setOptions={setOptions}
          />
        </Grid>
        <Grid item xs={12}>
          <Question
            questionText="¿Presenta delirios sólo durante la alteración del estado anímico?"
            question="question_12"
            setOptions={setOptions}
          />
        </Grid>
        {response !== null && "Enfermedad" in response && (
          <Grid item xs={12}>
            <Typography>{response.Enfermedad}</Typography>
          </Grid>
        )}
      </form>
    </Grid>
  );
};

export default Form;
