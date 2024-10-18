-- import data from metal_bands table
-- and ranks the countries origins of bands by number of non unique fans
SELECT
  origin,
  SUM(nb_fans) AS unique_fan_count
FROM
  metal_bands
GROUP BY
  origin
ORDER BY
  nb_fan DESC;