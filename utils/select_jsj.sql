SELECT *
FROM liwenhao.t_cj_ben
WHERE xh IN (SELECT xh FROM liwenhao."t_xsjbxxb_cs15-22");
