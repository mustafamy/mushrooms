DROP FUNCTION findcolors;
CREATE OR REPLACE FUNCTION findcolors(vlat float, vlon float, vKM integer)
RETURNS TABLE (cap_color  varchar, KM float) AS $$
DECLARE iw INT;
BEGIN

RETURN QUERY 
	select t1.cap_color, calculate_distance(vlat, vlon, lat, lon, 'K') 
	FROM mushrooms t1
	WHERE calculate_distance(vlat, vlon, lat, lon, 'K')  < vKM;
END;
$$ LANGUAGE plpgsql;