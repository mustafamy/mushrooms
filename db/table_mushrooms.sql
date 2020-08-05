CREATE TABLE public.mushrooms
(
    cap_shape character varying(50) COLLATE pg_catalog."default",
    cap_color character varying(50) COLLATE pg_catalog."default",
    odor character varying(50) COLLATE pg_catalog."default",
    gill_size character varying(50) COLLATE pg_catalog."default",
    gill_color character varying(50) COLLATE pg_catalog."default",
    stalk_color_above_ring character varying(50) COLLATE pg_catalog."default",
    veil_color character varying(50) COLLATE pg_catalog."default",
    ring_type character varying(50) COLLATE pg_catalog."default",
    spore_print_color character varying(50) COLLATE pg_catalog."default",
    population character varying(50) COLLATE pg_catalog."default",
    habitat character varying(50) COLLATE pg_catalog."default",
    lat numeric(10,5),
    lon numeric(10,5),
    ctime character varying(50) COLLATE pg_catalog."default"
)