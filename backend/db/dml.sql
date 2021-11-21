SELECT consultas.id, enfermedad.name as enfermedad
FROM consultas
JOIN enfermedad ON consultas.Enfermedad_id = enfermedad.id;