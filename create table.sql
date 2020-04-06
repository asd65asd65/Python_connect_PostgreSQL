CREATE TABLE public.prevent_disease
(
    id integer NOT NULL,
    name character varying COLLATE pg_catalog."default",
    temperature double precision NOT NULL,
    getmask boolean NOT NULL,
	date date NOT NULL,
    CONSTRAINT prevent_disease_pkey PRIMARY KEY (id)
)
insert into prevent_disease values(1,'a',36.6,true,'2020/04/04');
insert into prevent_disease values(2,'b',36.7,true,'2020/04/04');
insert into prevent_disease values(3,'c',36.0,true,'2020/04/04');
insert into prevent_disease values(4,'d',37.0,true,'2020/04/04');
insert into prevent_disease values(5,'e',37.0,false,'2020/04/04');
insert into prevent_disease values(6,'f',38.0,false,'2020/04/04');
insert into prevent_disease values(7,'g',38.1,true,'2020/04/04');
insert into prevent_disease values(8,'h',38.5,true,'2020/04/04');
insert into prevent_disease values(9,'i',38.2,true,'2020/04/04');
insert into prevent_disease values(10,'j',38.2,true,'2020/04/04');
select * from prevent_disease