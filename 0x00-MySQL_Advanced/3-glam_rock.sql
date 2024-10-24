-- selects bands with Glam rock style
-- and orders them by their lifespan
SELECT
  band_name,
  (2022 - formed) AS lifespan,
FROM
  metal_bands,
WHERE
  style = 'Glam rock',
ORDER BY
  lifespan DESC;