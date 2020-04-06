CREATE TABLE public.prevent_disease
(
    id integer NOT NULL,
    name character varying COLLATE pg_catalog."default",
    temperature double precision NOT NULL,
    getmask boolean NOT NULL,
    CONSTRAINT prevent_disease_pkey PRIMARY KEY (id)
)
insert into prevent_disease values(1,'a',36.6,true);
insert into prevent_disease values(2,'b',36.7,true);
insert into prevent_disease values(3,'c',36,true);
insert into prevent_disease values(4,'d',37,true);
insert into prevent_disease values(5,'e',37,false);
insert into prevent_disease values(6,'f',38,false);
insert into prevent_disease values(7,'g',38.1,true);
insert into prevent_disease values(8,'h',38.5,true);
insert into prevent_disease values(9,'i',38.2,true);
insert into prevent_disease values(10,'j',38.2,true);
select * from prevent_disease